# -*- coding: utf-8 -*-

from src.file_coordinates_extractor import FileCoordinatesExtractor

import unittest

class FileCoordinatesExtractorTest(unittest.TestCase):

    def test_extract_routes(self):
        coord_ext = FileCoordinatesExtractor()
        routes = coord_ext.extract_routes('test/coords_test_import.csv')
        self.assertEqual(1,len(routes))
        # = routes[0].stops[0]
        #self.assertEquals('Slut1',ro

    def test_extract_mult_routes(self):
        coord_ext = FileCoordinatesExtractor()
        routes = coord_ext.extract_routes('test/coords_test_import_mult.csv')
        self.assertEquals(3,len(routes))
