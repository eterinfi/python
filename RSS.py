# Filename: RSS.py
# -*- coding: utf-8 -*-

import urllib2
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		global Flag, Index
		if name == 'item':
			if Index == 0:
				News[Index] = { 'title' : Feed['title'], 'link' : Feed['link'] }
			Index += 1
		Flag = name

	def end_element(self, name):
		global Flag
		if name == 'item':
			News[Index] = { 'title' : Feed['title'], 'link' : Feed['link'], 'description' : Feed['description'], 'pubDate' : Feed['pubDate'] }
		if name == 'link':
			Flag = 'pubDate'
		else:
			Flag = None

	def char_data(self, text):
		global Feed, Flag
		if Flag in ('title', 'link', 'description', 'pubDate'):
			#if text.startswith('<') and text.endswith('>'):
			#	text = text[text.find('>') + 1 : text.rfind('<')]
			#elif text.startswith('<'):
			#	text = text[text.find('>') + 1 : ]
			Feed[Flag] = text

Feed = {}
News = {}
Index = 0
Flag = None

request = urllib2.Request("http://www.tsinghua.edu.cn/publish/news/rss/all.xml")
response = urllib2.urlopen(request)
w = response.read()
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(w)

print '%s @ %s' % (News[0]['title'], News[0]['link'])
i = 1
LineFeed = False
while i<=Index:
	if i < 10:
		print '(%d)%-80s' % (i, News[i]['title'][:39].encode('GB18030')),
	elif i > 99:
		print '(%d)%-78s' % (i, News[i]['title'][:39].encode('GB18030')),
	else:
		print '(%d)%-79s' % (i, News[i]['title'][:39].encode('GB18030')),
	if LineFeed:
		print
	i += 1
	LineFeed = not LineFeed
print
while True:
    ValidInput = False
    while not ValidInput:
    	print 'Select (1)~(%d) to view details, or (0) to quit:' % Index,
    	key = raw_input()
    	try:
    		i = int(key)
    		if i >= 0 and i <= Index:
    			ValidInput = True
    		else:
    			print 'Index must be a number between 0 and %d!\n' % Index
    	except ValueError:
    		print 'Index must be a number between 0 and %d!\n' % Index
    if i == 0:
    	break
    else:
    	print '\nNumber: %d' % i
    	print ' Title: %s' % News[i]['title'].encode('GB18030')
    	print 'Source: %s' % News[i]['link']
    	print '  Date: %s' % News[i]['pubDate']
    	print 'Header: %s\n' % News[i]['description'].encode('GB18030')