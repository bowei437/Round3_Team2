# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProblemsController(BaseTestCase):
    """ ProblemsController integration test stubs """

    def test_add_problem(self):
        """
        Test case for add_problem

        Creates a new problem and returns a problemID
        """
        response = self.client.open('/v3/',
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_problem(self):
        """
        Test case for delete_problem

        Delete Problem
        """
        response = self.client.open('/v3/id&#x3D;{problem_id}/'.format(problem_id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_problem(self):
        """
        Test case for get_problem

        Problems
        """
        response = self.client.open('/v3/id&#x3D;{problem_id}/'.format(problem_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
