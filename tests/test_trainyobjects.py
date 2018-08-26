import unittest

from app.model.trainyobjects import TrainStopp, Route, Connection

class TrainyObjectsTest(unittest.TestCase):

    def test_trainstop_geojson(self):
        stop = TrainStopp('Namny', 1.22, 60.4, 'Test describe', '1985-12-13')
        geoj = stop.getAsGeojson()
        self.assertEqual('Feature', geoj['type'])
        self.assertEqual('Namny', geoj['properties']['name'])
        self.assertEqual('Tågstation', geoj['properties']['amenity'])
        self.assertEqual('Test describ', geoj['properties']['popupContent'])
        self.assertEqual('1985-12-13', geoj['properties']['year'])
        self.assertEqual('Point', geoj['geometry']['type'])
        self.assertEqual([1.22, 60.4], geoj['geometry']['coordinates'])

    def test_connection_geojson(self):
        route = Route('R',1)
        stop = TrainStopp('Namny', 1.22, 60.4, 'Test describ', '1985-12-13')
        stop2 = TrainStopp('Namny2', 1.22, 63.4, 'Test describ2', '1985-12-13')
        c = Connection(stop, stop2, 1, route)
        geoj = c.getAsGeojson()
        self.assertEqual(2,len(geoj))

    def test_route_geojson(self):
        r = Route('Ro1', 1)
        stop = TrainStopp('Namny', 1.22, 60.4, 'Test describ', '1985-12-13')
        stop2 = TrainStopp('Namny2', 1.22, 63.4, 'Test describ2', '1985-12-13')
        c = Connection(stop, stop2, 2, r)
        r.connections.append(c)
        geoj = r.getAsGeojson()
        self.assertEqual(3,len(geoj))
