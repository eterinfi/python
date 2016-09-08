import time

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
    	global stack, L
    	L='';
    	for i in range(stack+1):
    		print(' '),
    	stack +=1
        print('<%s, attrs: %s>' % (name, [str(attrs) if len(str(attrs))<=100 else str(attrs)[:100]+'...']))
        #if 'China' in str(attrs): time.sleep(2)

    def end_element(self, name):
    	global stack, L
    	L=L.strip(' ').strip('\n')
    	if L:
    		for i in range(stack+1):
    			print(' '),
    		print('char_data: %s' % L)
    		L=''
    	stack -=1
    	for i in range(stack+1):
    		print(' '),
        print('</%s>' % name)

    def char_data(self, text):
    	global L
        #print('sax:char_data: %s' % text)
        L+=text

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

filename='latest.xml'
f=open(filename)
wasde=f.read()
f.close()
stack = 0
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
start=time.time()
parser.Parse(wasde)
end=time.time()
print('Time elpased: %.2fs' % (end-start))