from mctrainface.util.file_coordinates_extractor import FileCoordinatesExtractor
#from trainyobjects import TrainStopp, Route, Connection
import sys
import sqlite3

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

if __name__ == '__main__':
    pathy = sys.argv[1]
    ext = FileCoordinatesExtractor()
    route = ext.extract_route(pathy)
    conn = sqlite3.connect('src/routy/route.db')
    db = conn.cursor()
    crud = Crudder(db)
    crud.add_route(route)
    conn.commit()
