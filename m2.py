import requests
import re
import lxml.html
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup

#extarct links
def extractLinkRegEx(txt):
    tgs = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)
    return [match[1] for match in tgs.findall(txt)]

#another way to extract links
#using lxml 
def extractLinksLxml(txt):
    lst = []
    dom = lxml.html.fromstring(txt)
    for l in dom.xpath('//a/@href'):
        lst.append(l)
    return lst


#another way to extract links
#using htmlParser
def extractLinksHtmlParser(txt):
    lst = []
    dom = HTMLParser(txt)
    for tag in dom.tags('a'):
        attrs = tag.attributes
        if 'href' in attrs:
            lst.append(attrs['href'])
    return lst 


#another way to extract links
#using BeautifulSoup
def extractBs(txt):
    lst = []
    s =BeautifulSoup(txt, 'lxml')
    for tag in s.find_all('a', href=True):
        lst.append(tag['href'])
    
    return lst




def printList(lst):
    for l in lst:
        print('Level 1 -> ' + l)




r = requests.get('https://edfreitas.me')


#printList(extractLinkRegEx(r.text))
#printList(extractLinksLxml(r.text))
#printList(extractLinksHtmlParser(r.text))
printList(extractBs(r.text))