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

    def test_read_all(self):
        db = sqlite3.connect('instance/historailsdb.sqlite')
        crudder = Crudder(db)
        ro = crudder.get_all_routes()
        self.assertEqual(4,len(ro))
        
        self.assertEqual('Rutt1',ro[0].name)
        self.assertEqual(1,len(ro[0].connections))
        self.assertEqual('Kärrgruvan',ro[0].connections[0].node1.name)
        self.assertEqual('Ängelsberg station',ro[0].connections[0].node2.name)
        
        self.assertEqual('Rutt2',ro[1].name)
        self.assertEqual(1,len(ro[1].connections))
        self.assertEqual('Södertälje station',ro[1].connections[0].node1.name)
        self.assertEqual('Stockholm centralstation',ro[1].connections[0].node2.name)

        self.assertEqual('Rutt3',ro[2].name)
        self.assertEqual(1,len(ro[2].connections))
        self.assertEqual('Göteborg C',ro[2].connections[0].node1.name)
        self.assertEqual('Malmö Station',ro[2].connections[0].node2.name)
        
        self.assertEqual('Rutt4',ro[3].name)
        self.assertEqual(1,len(ro[3].connections))
        self.assertEqual('Nora station',ro[3].connections[0].node1.name)
        self.assertEqual('Örebro station',ro[3].connections[0].node2.name)
