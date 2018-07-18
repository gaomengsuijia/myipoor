# -*- coding: utf-8 -*-
__author__ = "hulinjun"
"""
程序运行入口
"""
import multiprocessing
from apscheduler.schedulers.background import BackgroundScheduler
from ipdoctor import Doctorip
from settings import CRON
import time

def main():
    """
    运行程序
    :return:
    """
    d = Doctorip()
    @aps.scheduled_job('cron',minute = CRON['minute'],hour = CRON['hour'],
                           day = CRON['day'],month = CRON['month'], week = CRON['week'])
    def task():
        print("oka")
        is_valid = multiprocessing.Process(target=d.is_valid)
        check_ip = multiprocessing.Process(target=d.check_ip)
        is_valid.start()
        check_ip.start()




if __name__ == '__main__':
    aps = BackgroundScheduler()
    try:
        main()
        print("开始定时任务..........")
        aps.start()
        while True:
            time.sleep(2)  # 其他任务是独立的线程执行
        print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        aps.shutdown()
    print('Exit The Job!')