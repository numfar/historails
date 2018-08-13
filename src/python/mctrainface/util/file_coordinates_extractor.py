# -*- coding: utf-8 -*-
import sys
import re

from mctrainface.model.trainyobjects import TrainStopp, Route, Connection

class FileCoordinatesExtractor(object):

    def extract_route(self,filename):
        route = Route()
        with open(filename,'r') as fileStream:
            stop_l = None
            for line in fileStream.readlines():
                if re.match('^<',line):
                    assert route.name is None
                    route.name = line.rsplit('<',1)[1].strip()
                else:
                    cols = line.split(',')
                    stop = TrainStopp(cols[0],int(cols[1]),int(cols[2]))
                    if stop_l is not None:
                        connection = Connection(stop_l,stop)
                        route.connections.append(connection)
                    stop_l = stop
        return route

if __name__ == '__main__':
    filename = sys.argv[1]
    ext = FileCoordinatesExtractor()
    route = ext.extract_route(filename)
    print(route.name)
    print(route.connections[0].node1.name)
    print(route.connections[0].node1.longitude)
    print(route.connections[0].node2.name)
    print(route.connections[0].node2.longitude)
