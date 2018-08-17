import re
import unittest
from unittest.mock import Mock, call
import sqlite3

from app.crud.cruddymodule import Crudder
from app.model.trainyobjects import Route, Connection, TrainStopp

class CrudderTest(unittest.TestCase):

    def test_add_route(self):
        db_mock = Mock()
        db_mock.fetchone.return_value = [1]
        crudder = Crudder(db_mock)
        route = Route()
        route.name = 'R1'
        stop1 = TrainStopp('s1',2,3)
        stop2 = TrainStopp('s2',5,6)
        connection = Connection(stop1,stop2)
        route.connections.append(connection)

        added_route = crudder.add_route(route)
        db_mock.execute.assert_has_calls([call("insert into stop ('stop_name','longitude','latitude') values ('s1','2','3')"),
                                           call("insert into stop ('stop_name','longitude','latitude') values ('s2','5','6')"),
                                           call("insert into route ('route_name') values ('R1')")], any_order=True)
