import base64

def safe_b64decode(s, altchars=None):
    while len(s) % 4 != 0:
        s += '='
    return base64.b64decode(s, altchars)

s = 'YWJjZA'
try:
    print 'Result: ', base64.b64decode(s)
except TypeError:
    print '(Safe-decoding)',
    print safe_b64decode(s)