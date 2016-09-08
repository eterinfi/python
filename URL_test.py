import urllib2

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http' : 'http://14.42.179.134:42932'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

request = urllib2.Request('https://www.google.com')
try:
    urllib2.urlopen(request,timeout = 10)
except urllib2.HTTPError, e:
    print 'HTTP_ERROR:', e.code, e.reason
except urllib2.URLError, e:
    print 'URL_ERROR:', e.reason
else:
    print 'OK'