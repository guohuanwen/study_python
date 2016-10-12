#coding:utf-8
import urllib
from collections import deque
from HTMLParser import HTMLParser
import re

_queue = deque(["http://www.baidu.com/s?wd=诛仙百度云"])
_opened_queue = deque([""])

def my_log(var,text):
    print(text)

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
    my_log(1,"open url")
    response = urllib.urlopen(url)
    HttpMessage = response.info()
    ContentType = HttpMessage.gettype()
    if "text/html" != ContentType:
        my_log(1,"is not text")
        return ""
    else:
        my_log(1,"read html")
        data = response.read()
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
    pattern = re.compile(r'^(https?|ftp|file)://.+$')
    yun_pattern = re.compile(r'https://pan.baidu.com.+$')
    
    while p<10000:
        p = p+1
        try :
            url = pull_url_unread();
            
            url_match = pattern.match(url)
            if url_match:
                my_log(0,url)
                print('\n')
            else:
                my_log(0,"is not url")
                continue
            
            html = openurl(url)
            if "" == html:
                my_log(0,"url is null")
                continue
            
            hp.feed(html)   
            for x in hp.links:
                yun_match = yun_pattern.match(x)
                if yun_match:
                    my_log(0,"find url "+x)
                push_queue_top(x)
            
            _opened_queue.append(url)
        except:
            continue

    hp.close()
    exit();

