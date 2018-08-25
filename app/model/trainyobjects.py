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

    def __init__(self,n1,n2,cid=None,route=None):
        self.node1 = n1
        self.node2 = n2
        self.cid = cid
        self.route = route

    def getAsGeojson(self):
        
        colly = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
	                "year": self.node1.start_year
                    },
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[self.node1.longitude,self.node1.latitude], [self.node2.longitude,self.node2.latitude]]
                    },
                    "id":str(self.cid) + "-" + str(self.route.rid)
                }]};
        return colly

    def getStopsAsGeojson(self):
        return [self.node1.getAsGeojson(), self.node2.getAsGeojson()];
    
class Route(object):
    
    def __init__(self, name=None, rid=None):
        self.rid = rid
        self.name = name
        self.connections = []

    def getAsGeojson(self):
        line = []
        for c in self.connections:
            line.extend(c.getStopsAsGeojson())
            line.append(c.getAsGeojson())
        return line
