# -*- coding: utf-8 -*-
__author__ = "hulinjun"
import redis
import threading
from Parsepage import Parsepage
from manaredis import Manaredis
from settings import DEYTIME
import time
class Poxy_metaclass(type):
    """
    元类，poxy类创建前，搜索出poxy类的所有ip爬虫，加入到attr中
    """
    def __new__(cls, name,bases,attrs):
        attrs['__crawlfun__']=[]
        for key,value in attrs.items():
            if "crawl_" in key:
                attrs['__crawlfun__'].append(key)
        attrs['_crfun__len'] = len(attrs['__crawlfun__'])
        return super(Poxy_metaclass, cls).__new__(cls, name,bases,attrs)



class Poxy(object,metaclass=Poxy_metaclass):
    """
     获取代理，放入redis中
    """

    def get_poxy_ip(self,backfun):
        """
        拿到代理ip
        :return:
        """
        poxy_ips = []
        for each in eval("self.{}()".format(backfun)):
            poxy_ips.append(each)

        return poxy_ips




    def crawl_1(self):
        """
        url = http://www.66ip.cn/index.html
        :return:
        """
        for page in range(1,2):
            url = "http://www.66ip.cn/{}.html".format(page)
            soup = Parsepage().get_page(url)
            trs = soup.select('#main tr')
            for i in range(1,len(trs)):
                poxy_ips = []
                for i in range(1,len(trs[i].contents)):
                    ip = trs[i].contents[0].text + ":" +  trs[i].contents[1].text
                    yield ip
            print("休息一下")
            time.sleep(2)

    # def crawl_2(self):
    #     """
    #     url = fdsaf
    #     :return:
    #     """
    #     return []


if __name__ == '__main__':
    p = Poxy()
    t = p.get_poxy_ip("crawl_1",[])
    print(t)
