import time
import urllib.request
import urllib.parse
from lxml import etree

class Spider():
    def __init__(self, header=None, **kwargs):
        if header is None:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        self.base_url = ""
        self.headers = headers
        self.xpath_details = '//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div[@class="text"]/text()'
        
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
        print(ret)
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
        ret0 = tree.xpath('//*[@id="main"]/div/div[3]/ul/li[1]/div/div[1]/h3/a/@href')
        
        # for i in range(1,len(ret)+1):
        for i in range(1,29):
            url = tree.xpath('//*[@id="main"]/div/div[3]/ul/li[' + str(i) + ']/div/div[1]/h3/a/@href')
            new_url = "https://www.zhipin.com" + url[0]
            response = self._request(new_url)
            self._parse_details(response)
        """
        new_url = self._parse(response0)
        response1 = self._request(new_url)
        # 转换
        result = response1.read().decode()
        tree = etree.HTML(result)
        ret = tree.xpath(self.xpath_details)
        print(ret)
        """
if __name__ == "__main__":
    spider = Spider()
    # 1到3年
    spider.run(base_url="https://www.zhipin.com/c101020100/e_104/?query=python&ka=sel-exp-104")
    # 3到5年
    #spider.run(base_url="https://www.zhipin.com/c101020100/e_105/?query=python&ka=sel-exp-105")


# print(tree)
# ret = tree.xpath('//div[@class="tang"]/ul/li[1]/text()')
# ret = tree.xpath('//div[@class="tang"]/ul/li[last()]/a/@href')
# ret = tree.xpath('//div[@class="tang"]/ul/li[@class="love" and @name="yang"]')
# ret = tree.xpath('//li[contains(@class,"l")]')
# ret = tree.xpath('//li[contains(text(),"爱")]/text()')
# ret = tree.xpath('//li[starts-with(@class, "ba")]/text()')

# ret = tree.xpath('//div[@class="song"]')
# string = ret[0].xpath('string(.)')
# print(string.replace('\n', '').replace('\t', ''))

#odiv = tree.xpath('//div[@class="tang"]')[0]

#ret = odiv.xpath('.//li[@class="balove"]')
#print(ret)