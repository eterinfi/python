# Filename: weatherX.py
# -*- coding: utf-8 -*-

import urllib2
from time import time, localtime, strftime
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		global china
		if name == 'city':
			china[attrs['pyName']] = {'cityname'      : attrs['quName'] if attrs['quName'] == attrs['cityname'] else attrs['quName'] + r'-' + attrs['cityname'], 
			                          'state1'        : attrs['state1'], 
			                          'state2'        : attrs['state2'], 
				                      'stateDetailed' : attrs['stateDetailed'], 
				                      'temp'          : attrs['tem1'] + r'/' + attrs['tem2'] + u' ℃', 
				                      'windState'     : attrs['windState']}

	def end_element(self, name):
		pass

	def char_data(self, text):
		pass

print u'当前时间：', strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
print '*' * 78
request = urllib2.Request("http://flash.weather.com.cn/wmaps/xml/china.xml")
response = urllib2.urlopen(request)
w = response.read()
china = {}
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(w)
for city in china:
	for item in ('cityname', 'temp', 'stateDetailed', 'windState'):
		print '%-17s' % china[city][item].encode('gbk'),
	print
print '*' * 78