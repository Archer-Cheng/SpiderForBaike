#-*- coding: UTF-8 -*-
'''
url_manager 类 url管理器
    self.new_urls  待爬取的URL契合
    self.old_urls  已爬取的URL集合
'''  
class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    #向管理器中添加一个url
    def add_new_url(self, url):
        if url is None:
            return
        #如果url不在待爬取的URL契合 也不再已爬取的URL集合 说明url是一个全新的url 将他放入 self.new_urls集合里
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #向管理器中添加批量url
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return 
        for url in urls:
            #调用单个添加方法
            self.add_new_url(url)
        
    #判断url管理器中是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0
    
    #获取url管理器中待爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    