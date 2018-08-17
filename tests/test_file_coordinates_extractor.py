# -*- coding: utf-8 -*-
import unittest

from app.util.file_coordinates_extractor import FileCoordinatesExtractor

class FileCoordinatesExtractorTest(unittest.TestCase):

    def test_extract_routes(self):
        coord_ext = FileCoordinatesExtractor()
        route = coord_ext.extract_route('tests/coords_test_import.csv')
        self.assertEqual('Route 1',route.name)
        self.assertEqual(1,len(route.connections))
        stop1 = route.connections[0].node1
        stop2 = route.connections[0].node2
        self.assertEqual('Slut1',stop1.name)
        self.assertEqual(1,stop1.longitude)
        self.assertEqual(34,stop1.latitude)
        self.assertEqual(4,stop2.longitude)
        self.assertEqual(45,stop2.latitude)
        self.assertEqual('Slut2',stop2.name)

