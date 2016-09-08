import sys, os, re

def search(s, dir):
    subdirs = [x for x in os.listdir(dir) if os.path.isdir(os.path.join(dir, x))]
    files   = [x for x in os.listdir(dir) if os.path.isfile(os.path.join(dir, x))]
    match   = [os.path.join(dir, x) for x in files if re.compile(s, re.I).search(os.path.splitext(x)[0])] # flag = IGNORECASE
    for sub in subdirs:
        try:
            match += search(s, os.path.join(dir, sub))
        except WindowsError, e:
            #print e
            pass
    return match

if __name__ == '__main__' and len(sys.argv)>1:
    key = sys.argv[1]
else:
    key = raw_input('Input Search Key: ')
result = search(key, '.')
for x in result:
    print os.path.abspath(x)
print 'Total File(s) Found:', len(result)