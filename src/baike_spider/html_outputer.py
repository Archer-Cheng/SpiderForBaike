#-*- coding: UTF-8 -*-  
'''
    写出数据
'''
class HtmlOutputer(object):
    def __init__(self):
        self.datas = [] 
    
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    #把数据输入到output.html
    def output_html(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        
        fout.write("<head >")
        fout.write('<meta content="text/html;charset=utf-8" http-equiv="content-type"/>')
        fout.write("</head>")
        
        fout.write("<body>")
        #将数据输出成一个表格格式
        fout.write("<table>")
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            #fout.write("<td>%s</td>" % data['content'].encode('utf-8'))
            fout.write("</tr>")
                
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        