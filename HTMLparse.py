import time
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global stack
        for i in range(stack):
            print(' '),
        stack+=1
        print('<%s, attrs:%s>' % (tag, str(attrs)))

    def handle_endtag(self, tag):
        global stack
        stack-=1
        for i in range(stack):
            print(' '),
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        global stack
        for i in range(stack):
            print(' '),
        print('<%s/, attrs:%s>' % (tag, str(attrs)))

    def handle_data(self, data):
        global stack
        for i in range(stack):
            print(' '),
        print(data)

    def handle_comment(self, data):
        global stack
        for i in range(stack):
            print(' '),
        print('<!-- -->')

    def handle_entityref(self, name):
        global stack
        for i in range(stack):
            print(' '),
        print('&%s;' % name)

    def handle_charref(self, name):
        global stack
        for i in range(stack):
            print(' '),
        print('&#%s;' % name)

stack = 0
parser = MyHTMLParser()
#parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br/>END</p></body></html>')
filename=('latest.xml')
f=open(filename)
while True:
    l=f.readline()
    if not l:
        break
    parser.feed(l)
f.close()