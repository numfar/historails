import sys
import sqlite3

from app.model.trainyobjects import Route, TrainStopp, Connection

class Crudder(object):

    def __init__(self,db):
        self.db = db
        self.rowid_query = "SELECT last_insert_rowid()"

    def add_route(self,route):
        sql_r = "insert into route ('route_name') values ('{}')".format(route.name)
        self.db.execute(sql_r)
        self.db.execute(self.rowid_query)
        id_r = self.db.fetchone()[0]

        for i,c in enumerate(route.connections):
            sql_x = "insert into stop ('stop_name','longitude','latitude') values ('{}','{}','{}')".format(c.node1.name,c.node1.longitude,c.node1.latitude)
            self.db.execute(sql_x)
            self.db.execute(self.rowid_query)
            id_c_x = self.db.fetchone()[0]
            sql_y = "insert into stop ('stop_name','longitude','latitude') values ('{}','{}','{}')".format(c.node2.name,c.node2.longitude,c.node2.latitude)
            self.db.execute(sql_y)
            self.db.execute(self.rowid_query)
            id_c_y = self.db.fetchone()[0]
            sql_c = "insert into connections ('node1','node2','route') values ('{}','{}','{}')".format(id_r,id_c_x,id_c_y)
            self.db.execute(sql_c)
        return route

    def get_all_routes(self):
        routes = []
        sql_all_r = "SELECT id,route_name FROM route r"
        for row in self.db.execute(sql_all_r).fetchall():
            r = Route(row[1])
            sql_all_c = "SELECT c.node1,c.node2 from connection c WHERE route = '{}'".format(row[0])
            for c_row in self.db.execute(sql_all_c).fetchall():
                sql_n = "SELECT * FROM stop WHERE id = '{}'"
                r_n1 = self.db.execute(sql_n.format(c_row[0])).fetchone()
                n1 = TrainStopp(r_n1[1],r_n1[5],r_n1[6],r_n1[3],r_n1[4])
                r_n2 = self.db.execute(sql_n.format(c_row[1])).fetchone()
                n2 = TrainStopp(r_n2[1],r_n2[5],r_n2[6],r_n2[3],r_n2[4])
                c = Connection(n1,n2)
                r.connections.append(c)
            routes.append(r)
        return routes
            
