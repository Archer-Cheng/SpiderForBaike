#-*- coding: UTF-8 -*-  
'''
    html下载器
'''
import urllib2

class HtmlDownloader(object):

    def download(self, url):
        #判断url是否为空
        if url is None:
            return None
        #请求到url内容 放在response里
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        #返回下载的内容
        return response.read()