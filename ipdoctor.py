# -*- coding: utf-8 -*-
__author__ = "hulinjun"
import requests
import time
from manaredis import Manaredis
from Parsepage import Parsepage
from settings import MAXCOUNT,MINCOUNT
from Poxy import Poxy
import threading


class Manageip(object):
    """
    检查Ip是否可用
    """
    def __init__(self):
        self.__red = Manaredis()



    def is_over_max(self):
        """
        判断ip数量是否超出了最大值
        :return:
        """
        if self.__red.count() >= MINCOUNT:
            return True
        return False

    def test(self,poxy_ip,page):
        """
        检查ip可用
        :param poxy_ip:
        :return:
        """
        url = "http://www.baidu.com"
        flag = page.parse_baidu(url,poxy_ip)
        if flag == True:  # 可以用就保存到redis中
            self.__red.save(poxy_ip)


    def getip(self):
        """
        执行抓取ip保存到redis中
        :return:
        """
        p = Poxy()
        td = []
        for i in range(p._crfun__len):
            print(p.__crawlfun__[i])
            the = threading.Thread(target=self.insert_to_redis,args=(p.__crawlfun__[i],p))
            td.append(the)

        for each in td:
            each.start()
            each.join()


    def insert_to_redis(self,backfun,p):
        """
        插入redis
        :return:
        """
        #拿到ips
        poxy_ips = p.get_poxy_ip(backfun)
        #开始检测每一个是否可用
        page = Parsepage()
        for each_ip in poxy_ips:
            self.test(each_ip,page)



class Doctorip(object):

    def is_valid(self):
        """
        检查ip是否可用,通过访问百度首页
        url = http://www.baidu.com
        :param poxy_ip:
        :return:
        """
        red = Manaredis()
        count = red.count()
        if count==0:
            print("等待添加ip")
            time.sleep(5)

        poxy_ips = red.get(int(0.5*count))
        manaip = Manageip()
        page = Parsepage()
        #循环每个ip进行检查
        for each_ip in poxy_ips:
            manaip.test(each_ip,page)


    def check_ip(self):
        """
        添加ip
        :return:
        """
        red = Manaredis()
        count = red.count()
        if count < MINCOUNT:#ip池数量不足
            print("开始添加ip")
            manaip = Manageip()
            manaip.getip()
        else:
            print("ip池数量足够了，不需要抓取")




if __name__ == '__main__':
    d = Doctorip()
    d.check_ip()





















