# -*- coding: utf-8 -*-
__author__ = "hulinjun"
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError,RequestException
from settings import TESTTIMEOUT
class Parsepage(object):
    """
    解析网页
    """
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }


    def get_page(self,url):
        try:
            req = requests.get(url=url,headers = self.headers)
            soup = BeautifulSoup(req.text,'lxml')
            return soup
        except Exception as e:
            print("get页面失败")

    def parse_baidu(self,url,poxy_ip):
        """
        检查百度，判断是否可用
        :param url:
        :return:
        """
        if isinstance(poxy_ip, bytes):
            poxy_ip = poxy_ip.decode('utf-8')#redis里面保存的是byte类型
        real_proxy = 'http://' + poxy_ip
        proxies = {
            "http": real_proxy,
            # "https": real_proxy,
        }
        try:
            print("开始检测ip : {}".format(poxy_ip))
            req = requests.get(url=url,headers=self.headers,proxies=proxies,timeout=TESTTIMEOUT)
            if req.status_code == 200:
                print("可用")
                return True
            print("不可用")
            return False
        except RequestException:
            return False
            # raise Exception("连接百度检测错误")




