# This program will extract all the links from a webpage
import sys
import urllib2
import re
url="ubuntuforums.org"
sys.stdout.write("Wait a Minute its retrieving.")
try:
    if url[0:4]!="http":
        url="http://" + url
        f=(urllib2.urlopen(url)).read()
        k=re.findall('(href)="(\S+)"',f)
        k=set(k)
        print "The Links are:------------"
        for x in k:
            if len(x[1])>2:
                print x[1] +"\n"
except:
    print "NOT found plz check url"


        
