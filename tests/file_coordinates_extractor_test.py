# -*- coding: utf-8 -*-

from util.file_coordinates_extractor import FileCoordinatesExtractor

import unittest

class FileCoordinatesExtractorTest(unittest.TestCase):

    def test_extract_routes(self):
        coord_ext = FileCoordinatesExtractor()
        route = coord_ext.extract_route('tests/coords_test_import.csv')
        self.assertEquals('Route 1',route.name)
        self.assertEqual(1,len(route.connections))
        stop1 = route.connections[0].node1
        stop2 = route.connections[0].node2
        self.assertEquals('Slut1',stop1.name)
        self.assertEquals(1,stop1.x)
        self.assertEquals(34,stop1.y)
        self.assertEquals(4,stop2.x)
        self.assertEquals(45,stop2.y)
        self.assertEquals('Slut2',stop2.name)

