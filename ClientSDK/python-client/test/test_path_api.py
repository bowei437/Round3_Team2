# coding: utf-8

"""
    Team 2 Pathfinding API

    Calculates minimum path between points depending on user generated map input.

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.path_api import PathApi


class TestPathApi(unittest.TestCase):
    """ PathApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.path_api.PathApi()

    def tearDown(self):
        pass

    def test_get_path(self):
        """
        Test case for get_path

        Path
        """
        pass


if __name__ == '__main__':
    unittest.main()
