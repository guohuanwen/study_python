#coding:utf-8
import urllib.request
from collections import deque
from html.parser import HTMLParser  

_queue = deque(["http://a.codekk.com/"])
_opened_queue = deque([""])


#队首压入
def push_queue_top(url):
    _queue.appendleft(url)

#队尾压入
def push_queue_bottom(url):
    _queue.append(url)

#队首取出
def pull_queue_top():
    return _queue.popleft()

#队尾取出
def pull_queue_bottom():
    return _queue.pop()

#是否存在队列中
def is_in_queue(url):
    return url in _opened_queue

#取出一个未浏览的url
def pull_url_unread():
    while True:
        url = pull_queue_bottom();
        if not(is_in_queue(url)):
            return url
            

#打开url 返回一个html
def openurl(url):   
    data = urllib.request.urlopen(url).read()
    html = data.decode("UTF-8")
    return html

#解析网页中的html  返回url list
class MyHTMLParser(HTMLParser):
    
    def __init__(self):   
        HTMLParser.__init__(self)   
        self.links = []
        
    def handle_starttag(self, tag, attrs):   
        #print "Encountered the beginning of a %s tag" % tag   
        if tag == "a":   
            if len(attrs) == 0:   
                pass   
            else:   
                for (variable, value) in attrs:   
                    if variable == "href":   
                        self.links.append(value)  
    

    

if __name__=="__main__":
    p = 1;
    hp = MyHTMLParser()   
    while p<30:
        try :
            url = pull_url_unread();
            print(url)
            print('\n')
            html = openurl(url)
            print (html)
            print('\n')
            
            hp.feed(html)   
            for x in hp.links:
                push_queue_top(x)
            
            _opened_queue.append(url)
            p = p+1
        except:
            continue

    hp.close()
    exit();

