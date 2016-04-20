#-*- coding: UTF-8 -*-
'''
目标：百度百科Python词条相关词条页面-标题和简介
入口页：http://baike.baidu.com/view/21087.htm
URL格式：
-词条页面URL：/view/125370.htm
数据格式：
-标题
    <dd class="lemmaWgt-lemmaTitle-title"><h1>***<h1></dd>
-简介
    <div class="lemma-summary" label-module="lemmaSummary">***<div>
页面编码 UTF-8
'''  

'''
    spider_main类 爬虫的总调度类
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer

class SpiderMain(object):
    #构造函数 初始化各个对象
    def __init__(self):
        #初始化url管理器
        self.urls = url_manager.UrlManager()
        #初始化url下载器
        self.downloader = html_downloader.HtmlDownloader()
        #初始化url解析器
        self.parser = html_parser.HtmlParser()
        #初始化输出类
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self, root_url):
        count = 1
        #在url管理器中添加入口url
        self.urls.add_new_url(root_url)
         
        #启动爬虫的循环
        #当url管理器中有url时进入循环
        while self.urls.has_new_url():
            # try 出现问题 输出一个craw failed
            try:
                #获取到待爬取的url
                new_url = self.urls.get_new_url()
                #输出 当前爬取得页面是第几个页面及其它的 url
                print 'craw %d : %s' %(count,new_url)
                #下载这个页面
                html_cont = self.downloader.download(new_url)
                #调用解析器 解析这个页面 得到新的页面
                new_urls, new_data =self.parser.parse(new_url, html_cont)
                #将解析器解析出的urls补充如url管理器
                self.urls.add_new_urls(new_urls)
                #收集数据
                self.outputer.collect_data(new_data)
                
                #if self.urls.get_new_url() == suoyin:
                    #break
                if count == 100:
                    break
                count = count + 1
            except:
               print 'craw failed'
        self.outputer.output_html()
    
    
    
'''
主函数
调用craw（）  启动爬虫
root_url 设置爬虫的入口URL
'''
if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    