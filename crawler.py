import sys
import time
import math
import urllib2
import urlparse
from urllib import *
from urllib.parse import urlparse
import optparse
import hashlib
from cgi import escape
from traceback import format_exc
from Queue import Queue, Empty as QueueEmpty
from queue import Queue, Empty as QueueEmpty
from bs4 import BeautifulSoup
 
class Crawler(object):
 
     def __init__(self, root, depth_limit, confine=None, exclude=[], locked=True, filter_seen=True):
         self.root = root
         self.host = urlparse.urlparse(root)[1]
         self.host = urlparse(root)[1]
 
         ## Data for filters:
         self.depth_limit = depth_limit # Max depth (number of hops from root)
     def _pre_visit_url_condense(self, url):
         #so that http://foo.com/blah.html\#baz becomes
         #http://foo.com/blah.html """
         base, frag = urlparse.urldefrag(url)
         base, frag = urllib.parse.urldefrag(url)
         return base
 
     ## URL Filtering functions.  These all use information from the
     def _not_visited(self, url):
            print "moses"
	
     def _same_host(self, url):
         """Pass if the URL is on the same host as the root URL"""
         try:
	     host = urlparse.urlparse(url)[1]
             host = urlparse(url)[1]
             return re.match(".*%s" % self.host, host) 
         except Exception, e:
             print >> sys.stderr, "ERROR: Can't process url '%s' (%s)" % (url, e)
         except Exception as e:
             print(sys.stderr, "ERROR: Can't process url '%s' (%s)" % (url, e))
             return False
             
 
     def crawl(self):
             
             #Special-case depth 0 (starting URL)
             if depth == 0 and [] != do_not_follow:
                 print >> sys.stderr, "Whoops! Starting URL %s rejected by the following filters:", do_not_follow
                 print(sys.stderr, "Whoops! Starting URL %s rejected by the following filters:", do_not_follow)
 
             #If no filters failed (that is, all passed), process URL
             if [] == do_not_follow:
                def crawl(self):
                            
                    link = Link(this_url, link_url, "href")
                    try:
                        if link not in self.links_remembered:
                                                                                   
                            self.links_remembered.add(link)
                            print "moses"
                            
                    except Exception, e:
                            print >>sys.stderr, "ERROR: Can't process url '%s' (%s)" % (this_url, e)
                    except Exception as e:
                            print(sys.stderr, "ERROR: Can't process url '%s' (%s)" % (this_url, e))
                    #print format_exc()
     
class OpaqueDataException (Exception):
	def _addHeaders(self, request):
             def _open(self):
                 url = self.url
                 try:
                     request = urllib2.Request(url)
                     handle = urllib2.build_opener()
                     request = urllib.request.urlopen(url).read()
                     handle = urllib.build_opener()
                 except IOError:
                     return None
                 return (request, handle)
             def fetch(self):
                    try:
                         errors="replace"
                         soup = BeautifulSoup(content)
                         tags = soup('a')
                         
                     except urllib2.HTTPError, error:
                         print >> sys.stderr, "ERROR: %s -> %s" % (error, error.url)
                     except urllib.HTTPError as error:
                         if error.code == 404:
                             print >> sys.stderr, "ERROR: %s -> %s" % (error, error.url)
                             print(sys.stderr, "ERROR: %s -> %s" % (error, error.url))
                         else:
                             print >> sys.stderr, "ERROR: %s" % error
                             print(sys.stderr, "ERROR: %s" % error)
                         tags = []
                     except urllib2.URLError, error:
                         print >> sys.stderr, "ERROR: %s" % error
                     except urllib.URLError as error:
                         print(sys.stderr, "ERROR: %s" % error)
                         tags = []
                     except OpaqueDataException, error:
                         print >>sys.stderr, "Skipping %s, has type %s" % (error.url, error.mimetype)
                     except OpaqueDataException as error:
                         print(sys.stderr, "Skipping %s, has type %s" % (error.url, error.mimetype))
                         tags = []
                     for tag in tags:
                         href = tag.get("href")
                         if href is not None:
                             url = urlparse.urljoin(self.url, escape(href))
                             url = urllib.parse.urljoin(self.url, escape(href))
                             if url not in self:
                                 self.out_urls.append(url)
 
 def getLinks(url):
     page = Fetcher(url)
     page.fetch()
     for i, url in enumerate(page):
         print "%d. %s" % (i, url)
         print("%d. %s" % (i, url))
 
 def parse_options():
     """parse_options() -> opts, args"""
  def parse_options():
 
     if len(args) < 1:
         parser.print_help(sys.stderr)
         raise SystemExit, 1
        raise SystemExit(1)
 
     if opts.out_links and opts.out_urls:
         parser.print_help(sys.stderr)
	def _safe_alias(self, url, silent=False):
             name = "N"+m.hexdigest()
             self.node_alias[url]=name
             if not silent:
                 print "\t%s [label=\"%s\"];" % (name, url)                
                 print("\t%s [label=\"%s\"];" % (name, url))
             return name
 
 
     def asDot(self, links):
 
         """ Render a collection of Link objects as a Dot graph"""
         
         print "digraph Crawl {"
         print "\t edge [K=0.2, len=0.1];"
         print("digraph Crawl {")
         print("\t edge [K=0.2, len=0.1];")
         for l in links:            
             print "\t" + self._safe_alias(l.src) + " -> " + self._safe_alias(l.dst) + ";"
         print  "}"
             print("\t" + self._safe_alias(l.src) + " -> " + self._safe_alias(l.dst) + ";")
         print("}")
 
         
     
def main():
 
     if opts.links:
         getLinks(url)
         raise SystemExit, 0
         raise SystemExit(0)
 
     depth_limit = opts.depth_limit
     confine_prefix=opts.confine
     exclude=opts.exclude
 
     sTime = time.time()
 
     print >> sys.stderr,  "Crawling %s (Max Depth: %d)" % (url, depth_limit)
     print(sys.stderr,  "Crawling %s (Max Depth: %d)" % (url, depth_limit))
     crawler = Crawler(url, depth_limit, confine_prefix, exclude)
     crawler.crawl()
 
     if opts.out_urls:
         print "\n".join(crawler.urls_seen)
         print("\n".join(crawler.urls_seen))
 
     if opts.out_links:
         print "\n".join([str(l) for l in crawler.links_remembered])
         print("\n".join([str(l) for l in crawler.links_remembered]))
         
     if opts.out_dot:
         d = DotWriter()
  def main():
     eTime = time.time()
     tTime = eTime - sTime
 
     print >> sys.stderr, "Found:    %d" % crawler.num_links
     print >> sys.stderr, "Followed: %d" % crawler.num_followed
     print >> sys.stderr, "Stats:    (%d/s after %0.2fs)" % (
             int(math.ceil(float(crawler.num_links) / tTime)), tTime)
     print(sys.stderr, "Found:    %d" % crawler.num_links)
     print(sys.stderr, "Followed: %d" % crawler.num_followed)
     print(sys.stderr, "Stats:    (%d/s after %0.2fs)" % (int(math.ceil(float(crawler.num_links) / tTime)), tTime))
 
 if __name__ == "__main__":
     main()
