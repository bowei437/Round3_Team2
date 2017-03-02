# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.boundary import Boundary
from swagger_server.models.error import Error
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestBoundaryController(BaseTestCase):
    """ BoundaryController integration test stubs """

    def test_get_boundary(self):
        """
        Test case for get_boundary

        Boundary
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/Boundary'.format(problem_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_boundary(self):
        """
        Test case for update_boundary

        Update the existing boundary value
        """
        boundary = Boundary()
        response = self.client.open('/v2/id&#x3D;{problem_id}/Boundary/ver&#x3D;{version}/'.format(problem_id=56, version=1.2),
                                    method='PUT',
                                    data=json.dumps(boundary),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
