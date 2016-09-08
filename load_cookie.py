import urllib2
import cookielib
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar() # Declare a MozillaCookieJar object instance
cookie.load(filename, ignore_discard = True, ignore_expires = True) # Load cookie file to object
handler = urllib2.HTTPCookieProcessor(cookie) # Create cookie processor using urllib2.HTTPCookieProcessor object
opener = urllib2.build_opener(handler) # Build opener through handler
response = opener.open('http://www.zhihu.com') # Equal to urllib2.urlopen method
print response.read()