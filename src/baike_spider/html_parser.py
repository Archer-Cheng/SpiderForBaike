#-*- coding: UTF-8 -*-
'''
    html解析器
'''  
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    
    #获取页面里的词条url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 得到 格式为  /view/123.htm  的词条URL
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        
        for link in links:
            new_url = link['href']
            #凭借完整的url
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
        
        
    #解析数据
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        #url 
        res_data['url'] = page_url
        
        #解析title <dd class="lemmaWgt-lemmaTitle-title"> <h1>爬虫</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find()
        res_data['title'] = title_node.get_text()
        
        #解析简介 <div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        '''
        #解析内容 <div class="content">
        summary_node = soup.find('div', class_="main-content")
        res_data['content'] = summary_node.get_text()
        '''
        
        
        return res_data
        
        
    #解析
    def parse(self, page_url,html_cont):
        if page_url is None or html_cont is None:
            return 
        
        soup = BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data