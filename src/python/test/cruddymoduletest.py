from src.routy.cruddymodule import Crudder
from src.routy.trainyobjects import Route, Connection, TrainStopp

import re
import unittest

class DbMock(object):

    def __init__(self):
        self.commands = []

    def execute(self,command):
        self.commands.append(command)

class CrudderTest(unittest.TestCase):

    def test_add_route(self):
        db_mock = DbMock()
        crudder = Crudder(db_mock)
        route = Route()
        route.name = 'R1'
        stop1 = TrainStopp('s1',2,3)
        stop2 = TrainStopp('s2',5,6)
        connection = Connection(stop1,stop2)
        route.connections.append(stop1)
        route.connections.append(stop2)

        added_route = crudder.add_route(route)
        self.assertEquals(
            "insert into stop ('name','longitude','latitude') values ('s1','2','3')",
            db_mock.commands[0])
        self.assertEquals(
            "insert into stop ('name','longitude','latitude') values ('s2','5','6')",
            db_mock.commands[1])
        self.assertEquals(
            "insert into route ('name') values ('R1')",
            db_mock.commands[2])
