# -*- coding: utf-8 -*-
import sys
import re

class TrainStopp(object):

    def __init__(self,name,x,y):
        self.name = name
        self.longitude = x
        self.latitude = y

class Connection(object):

    def __init__(self,n1,n2):
        self.node1 = n1
        self.node2 = n2

class Route(object):

    def __init__(self):
        self.name = None
        self.connections = []
