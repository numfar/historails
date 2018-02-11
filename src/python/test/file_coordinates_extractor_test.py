# -*- coding: utf-8 -*-

from src.file_coordinates_extractor import FileCoordinatesExtractor

import unittest

class FileCoordinatesExtractorTest(unittest.TestCase):

    def test_extract_routes(self):
        coord_ext = FileCoordinatesExtractor()
        route = coord_ext.extract_route('test/coords_test_import.csv')
        self.assertEqual(2,len(route.stops))
        stop1 = route.stops[0]
        stop2 = route.stops[1]
        self.assertEquals('Slut1',stop1.name)
        self.assertEquals(1,stop1.x)
        self.assertEquals(34,stop1.y)
        self.assertEquals(4,stop2.x)
        self.assertEquals(45,stop2.y)
        self.assertEquals('Slut2',stop2.name)

