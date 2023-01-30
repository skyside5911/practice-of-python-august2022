# to find the numbers in the site using webscraping and re module
import re,urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
numbers=re.findall('[0-9]{3,4}[- ][0-9-]+',str(text))
for n in numbers:
    print(n)