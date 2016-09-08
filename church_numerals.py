def p(*args): print "This is a line."
def q(*args): print "This is another line. "

def zero(f):
    def zerox(x=None):
        return x
    return zerox

def one(f):
    def onex(x=None):
        return f(x)
    return onex

def plus(m, n):
    def plusf(f=None):
        def plusx(x=None):
            return m(f)(n(f)(x))
        return plusx
    return plusf

def succ(n):
    def succf(f=None):
        def succx(x=None):
            return f(n(f)(x))
        return succx
    return succf

def mult(m, n):
    def multf(f=None):
        return n(m(f))
    return multf

def exp(m, n):
    return n(m);

def pred(n):
    def predf(f=None):
        def predx(x=None):
            def predg(g=None):
                def predh(h=None):
                    return h(g(f))
                return predh
            def predu1(u=None):
                return x
            def predu2(u=None):
                return u
            return n(predg)(predu1)(predu2)
        return predx
    return predf