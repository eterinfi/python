import urllib2
import cookielib
cookie = cookielib.CookieJar() # Declare a CookieJar object instance to save cookie
handler = urllib2.HTTPCookieProcessor(cookie) # Create cookie processor using urllib2.HTTPCookieProcessor object
opener = urllib2.build_opener(handler) # Build opener through handler
response = opener.open('http://www.zhihu.com') # Equal to urllib2.urlopen method
for item in cookie:
    print 'Name = %s, Value = %s' % (item.name, item.value)