# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/09/18 上午8:25
describe: 队列
"""
class Queue:
    def __init__(self):
        self.alist =[]

    def enqueue(self,value):
        self.alist.index(0,value)

    def dequeue(self):
        self.alist.pop()

    def isEmpty(self):
        return  self.alist == []

    def size(self):
        return len(self.alist)