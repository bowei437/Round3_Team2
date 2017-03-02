# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.goal import Goal
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGoalController(BaseTestCase):
    """ GoalController integration test stubs """

    def test_get_goal(self):
        """
        Test case for get_goal

        Goal Location
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/Goal'.format(problem_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_goal(self):
        """
        Test case for update_goal

        Update the existing goal value
        """
        goal = Goal()
        response = self.client.open('/v2/id&#x3D;{problem_id}/Goal/ver&#x3D;{version}/'.format(problem_id=56, version=1.2),
                                    method='PUT',
                                    data=json.dumps(goal),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
