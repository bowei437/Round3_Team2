# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.path import Path
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPathController(BaseTestCase):
    """ PathController integration test stubs """

    def test_get_path(self):
        """
        Test case for get_path

        Path
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/Path'.format(problem_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
