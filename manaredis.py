# -*- coding: utf-8 -*-
__author__ = "hulinjun"
from settings import REDIS
import redis
from error import PooremptyError
class Manaredis(object):
    """
    redis操作
    """

    def __init__(self):
        self.host = REDIS['host']
        self.port = REDIS['port']
        self.password = REDIS['password'] if 'password' in REDIS else None
        if self.password:
            self.redisclient = redis.Redis(host=self.host,port=self.port,password=self.password)
        else:
            self.redisclient = redis.Redis(host=self.host, port=self.port)


    def get(self,count):
        """
        get操作，取出来用于验证ip是否可用
        :return:
        """
        poxy_ips = self.redisclient.lrange("poxy_ip",0,count - 1)
        self.redisclient.ltrim("poxy_ip",0,count-1)#这里取出来就直接清除了哦哦哦，验证如果可以会重新push进去
        return poxy_ips

    def save(self,poxy_ip):
        """
        save操作,从ip网站获取的保存下来
        :return:
        """
        self.redisclient.rpush("poxy_ip",poxy_ip)
        print("插入成功")

    def pop(self):
        """
        给接口获取
        :return:
        """
        try:
            poxy_ip = self.redisclient.rpop("poxy_ip")
            return poxy_ip
        except Exception:
            raise PooremptyError

    def count(self):
        """
        得到ip的总数
        :return:
        """
        return self.redisclient.llen("poxy_ip")



if __name__ == '__main__':
    red = Manaredis()
    r = red.count()
    print(r)