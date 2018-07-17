# -*- coding: utf-8 -*-
__author__ = "hulinjun"

class PooremptyError(Exception):
    """
    ip池获取不到ip的错误
    """
    def __init__(self):
        Exception.__init__()


    def __str__(self):
        return repr("poor is empty")