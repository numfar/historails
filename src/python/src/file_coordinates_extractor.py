# -*- coding: utf-8 -*-

class TrainStopp(object):

    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        self.name = name

class Route(object):

    def __init__(self,name):
        self.name = name
        self.stops = []

class FileCoordinatesExtractor(object):

    def extract_routes(self,filename):
        routes = []
        with open(filename,'r') as fileStream:
            for line in fileStream.readlines():
                routes.append(line)
        return routes
