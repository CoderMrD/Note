import time
import sys
import pandas as pd
import urllib.request
import urllib.parse

from lxml import etree

class Spider():
    def __init__(self, header=None, **kwargs):
        if header is None:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        self.base_url = ""
        self.headers = headers
        self.xpath_details = '//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div[@class="text"]/text()'
        self.xpath_campany_name = '//*[@id="main"]/div/div[3]/ul/li[2]/div/div[2]/div/h3/a'
        self.xpath_salary = '//*[@id="main"]/div/div[3]/ul/li[2]/div/div[1]/h3/a/span'
        self.xpath_position = '//*[@id="main"]/div/div[3]/ul/li[8]/div/div[1]/h3/a/div[1]'
        
    def _parse_list(self, response, xpath):
        result = response.read().decode()
        tree = etree.HTML(result)
        ret = tree.xpath(xpath)
        new_url = "https://www.zhipin.com" + ret[0]
        return new_url

    def _parse_details(self, response):
        result = response.read().decode()
        tree = etree.HTML(result)
        ret = tree.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div/text()')
        return ret
        
    def _request(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)
        response = urllib.request.urlopen(request)
        return response
    
    def urlJoin(self):
        pass
        
    def run(self, base_url=None):
        self.base_url = base_url
        response0 = self._request(self.base_url)
        xpath = '//*[@id="main"]/div/div[3]/ul/li'
        
        result = response0.read().decode()
        tree = etree.HTML(result)
        ret = tree.xpath(xpath)
        print(len(ret))
        # url
        # print(ret[0].xpath('./div[@class="job-primary"]/div/h3[@class="name"]/a/@href'))
        # 公司
        # print(ret[0].xpath('./div/div[@class="info-company"]/div/h3/a/text()'))
        # 薪资
        # xpath('./div/div[1]/h3/a/span')
        # 岗位
        # xpath('./div/div[1]/h3/a/div[@class="job-title"]')
        i = 0
        df1 = pd.DataFrame(columns = ['公司','职位','薪资','岗位要求'])
        for li in ret:
            i = i + 1
            url = tree.xpath('//*[@id="main"]/div/div[3]/ul/li[' + str(i) + ']/div/div[1]/h3/a/@href')
            new_url = "https://www.zhipin.com" + url[0]
            time.sleep(3)
            response = self._request(new_url)
            description = str(self._parse_details(response)).replace(" ","").replace(r"\n","").replace("'","").replace("n","")
            #description = description.replace(r"\n","").replace(" ","")
            salary = str(li.xpath('./div/div[@class="info-primary"]/h3/a/span/text()')[0])
            position = str(li.xpath('./div/div[1]/h3/a/div[@class="job-title"]/text()')[0])
            company = str(li.xpath('./div/div[@class="info-company"]/div/h3/a/text()')[0])
            print(str(company))
            new=pd.DataFrame({'公司':company,
                  '职位':position,
                  '薪资':salary,
                  '岗位要求':description},
                  index=[1])
            df1 = df1.append(new)
        writer=pd.ExcelWriter('‪test.xlsx')   
        df1.to_excel(writer,sheet_name='Data1',startcol=0,index=False)
        writer.save()
        
if __name__ == "__main__":
    spider = Spider()
    # 1到3年
    spider.run(base_url="https://www.zhipin.com/c101020100/e_104/?query=python&ka=sel-exp-104")
    # 3到5年
    #spider.run(base_url="https://www.zhipin.com/c101020100/e_105/?query=python&ka=sel-exp-105")
