import os
import sys
import ssl
import json
import requests
import unittest
from  pathfinder import *
from latLongConversion import *
 

class Test(unittest.TestCase):
             
        def testLatitudeConversion(self):
            """
            Test Latitude Longitude Conversion
            """
            r = convert_latlong_to_xy(37.229572, 7)
            self.assertEqual(r, 372295720)

        def testLongitudeConversion(self):
            """
            Test Longitude Conversion"
            """
            r = convert_latlong_to_xy(-80.413940, 7)
            self.assertEqual(r, -804139400)



if __name__ == '__main__':
    unittest.main()