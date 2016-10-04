from math import log
from data import playgolf

dvar = "PLAY"

f = {
    "OUTLOOK":     ( lambda x: x == "sunny", lambda x: x == "overcast",   lambda x: x == "rain" ),
    "TEMPERATURE": ( lambda x: x < 70,       lambda x: x in range(70,80), lambda x: x >= 80 ),
    "HUMIDITY":    ( lambda x: x > 70,       lambda x: x <= 70 ),
    "WIND":        ( lambda x: not x,        lambda x: x )
}

q = {
    "OUTLOOK":     ( "sunny", "overcast", "rain" ),
    "TEMPERATURE": ( "cool",  "mild",     "hot" ),
    "HUMIDITY":    ( "high",  "normal" ),
    "WIND":        ( "false",  "true" )}

class Node(object):
    def __init__(self, u, s, dep_var=dvar):
        self.u = u
        if '/' in u:
            cd = u.split('/')[-1].split('=')
            self.a = cd[0]
            self.v = cd[1]
        else:
            self.a = None
            self.v = None
        self.s = s
        self.p = len(yes(s, dep_var))
        self.n = len(no(s, dep_var))
        self.parent = None
        self.children = []

def yes(s, var):
    return filter(lambda x: x[var], s)

def no(s, var):
    return filter(lambda x: not x[var], s)

def entropy(s, dep_var=dvar):
    t = float(len(s))
    p = len(yes(s, dep_var))
    e = -(p/t) * log(p/t, 2) if p > 0 else 0
    n = len(no(s, dep_var))
    e -= (n/t) * log(n/t, 2) if n > 0 else 0
    return e

def gain(s, indep_var, f, dep_var=dvar):
    t = float(len(s))
    g = entropy(s)
    group = list()
    for i in range(len(f)):
        group.append(filter(lambda x: f[i](x[indep_var]), s))
        g -= (len(group[i])/t)*entropy(group[i])
    return g

def gnode(cnode, pr):
    if cnode.n and not cnode.p:
        nset.append(cnode)
        return
    elif cnode.p and not cnode.n:
        pset.append(cnode)
        return
    elif not pr or len(cnode.u.split('/')) > 3:
        uset.append(cnode)
        return
    else:
        dset.append(cnode)
    pick = max(pr.values())
    npr = {}
    for key in pr:
        if pr[key] == pick:
            attr = key
        else:
            npr[key] = pr[key]
    for fx in f[attr]:
        fs = filter(lambda x: fx(x[attr]), cnode.s)
        if not fs:
            continue
        value = q[attr][f[attr].index(fx)]
        path = cnode.u + "/" + attr + "=" + value
        snode = Node(path, fs)
        snode.parent = cnode
        cnode.children.append(snode)
        gnode(snode, npr)
    return

def pnode(cnode, indent=0):
    ws = " "*indent
    if not cnode.a:
        print "%sROOT S(%d+, %d-)" % (ws, cnode.p, cnode.n)
    else:
        print "%s/%s=%s: S(%d+, %d-)" % (ws, cnode.a, cnode.v, cnode.p, cnode.n)
    for node in cnode.children:
        pnode(node, indent+2)
    return

def pclass(classes, sets):
    for i in range(len(sets)):
        print "\n%s:" % classes[i]
        if sets[i]:
            for node in sets[i]:
                print "  S(%d+, %d-) %s" % (node.p, node.n, node.u)
        else:
            print "  Empty Set"
    return
    
prop = {}
for key in f:
    prop[key] = gain(playgolf, key, f[key])
    print "Gain[%s] = %f" % (key, prop[key])

root = Node("~", playgolf)
pset = []; nset = []; uset = []; dset = []
gnode(root, prop)
print
pnode(root)
classes = ["Play", "Don't play", "Undecided", "Divisble"]
sets = [pset, nset, uset, dset]
pclass(classes, sets)