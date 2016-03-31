# Project : show me the code
# Author : puorc
# Powered by PyQuery and target site: http://www.meizitu.com
from pyquery import PyQuery as pq
import urllib


def get_content_links(url):
    content_links = []
    parser = pq(url)
    divs = parser('#picture')
    links = divs('a')
    for i in links:
        tmp = pq(i)
        content_links.append(tmp.attr['href'])
    return content_links


def download_pics(url):
    pic_link = []
    parser = pq(url)
    divs = parser('#picture')
    links = divs('img')
    for i in links:
        tmp = pq(i)
        pic_link.append(tmp.attr['src'])
    for i in pic_link:
        filename = i.split('/')[-4] + i.split('/')[-3] + i.split('/')[-2] + i.split('/')[-1]
        urllib.urlretrieve(i, filename)
    print 'Success! Enjoy it!'


for i in get_content_links('http://www.meizitu.com'):
    download_pics(i)
