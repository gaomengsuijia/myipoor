# -*- coding: utf-8 -*-
__author__ = "hulinjun"

#redis的配置信息
REDIS = {
    "host":"172.20.2.70",
    "port":6379,
}

#爬虫延迟时间
DEYTIME = 5

#ip池允许的最小数量ip
MINCOUNT = 500

#ip池允许的最大数量ip
MAXCOUNT = 1000
#测试百度的超时时间
TESTTIMEOUT = 2
#定时日程
CRON = {
    'minute':'36',
    'hour':'11',
    'day':'*',
    'month':'*',
    'week':'*'
}
