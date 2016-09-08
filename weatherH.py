# Filename: weatherH.py
# -*- coding: utf-8 -*-

import urllib2
from time import time, localtime, strftime
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        global china
        if tag == 'city':
            attrs = dict(attrs)    
            china[attrs['pyname']] = {'cityname'      : attrs['quname'].decode('utf-8') if attrs['quname'] == attrs['cityname'] else
                                                        attrs['quname'].decode('utf-8') + r'-' + attrs['cityname'].decode('utf-8'),
                                      'state1'        : attrs['state1'], 
                                      'state2'        : attrs['state2'], 
                                      'stateDetailed' : attrs['statedetailed'].decode('utf-8'), 
                                      'temp'          : attrs['tem1'] + r'/' + attrs['tem2'] + u' ℃', 
                                      'windState'     : attrs['windstate'].decode('utf-8')}

print u'当前时间：', strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
print '*' * 78
request = urllib2.Request("http://flash.weather.com.cn/wmaps/xml/china.xml")
response = urllib2.urlopen(request)
w = response.read()
china = {}
parser = MyHTMLParser()
parser.feed(w)
for city in china:
    for item in ('cityname', 'temp', 'stateDetailed', 'windState'):
        print '%-17s' % china[city][item].encode('gbk'),
    print
print '*' * 78
