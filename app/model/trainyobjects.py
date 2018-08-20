# -*- coding: utf-8 -*-
import sys
import re

class TrainStopp(object):

    def __init__(self,name,x,y,d=None,year=None):
        self.name = name
        self.longitude = x
        self.latitude = y
        self.description = d
        self.start_year = year

    def getAsGeojson(self):
        feature = {
            "type": "Feature",
            "properties": {
	        "name": self.name,
	        "amenity": "Tågstation",
	        "popupContent": self.description,
	        "year": self.start_year
            },
            "geometry": {
	        "type": "Point",
	        "coordinates": [self.longitude, self.latitude]
            }
        };
        return feature;

class Connection(object):

    def __init__(self,n1,n2):
        self.node1 = n1
        self.node2 = n2

    def getAsGeojson(self):
        return [self.node1.getAsGeojson(), self.node2.getAsGeojson()];

class Route(object):
    
    def __init__(self, name=None):
        self.name = name
        self.connections = []

    def getAsGeojson(self):
        line = []
        for c in self.connections:
            line.extend(c.getAsGeojson())
        return line
