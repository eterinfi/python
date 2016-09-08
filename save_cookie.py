import urllib2
import cookielib
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename) # Declare a MozillaCookieJar object instance to save cookie and write to file
handler = urllib2.HTTPCookieProcessor(cookie) # Create cookie processor using urllib2.HTTPCookieProcessor object
opener = urllib2.build_opener(handler) # Build opener through handler
response = opener.open('http://www.zhihu.com') # Equal to urllib2.urlopen method
cookie.save(ignore_discard = True, ignore_expires = True)