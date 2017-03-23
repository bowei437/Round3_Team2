# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.robot import Robot
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestRobotController(BaseTestCase):
    """ RobotController integration test stubs """

    def test_add_robot(self):
        """
        Test case for add_robot

        Add a new robot to the list
        """
        robot = Robot()
        response = self.client.open('/v2/id&#x3D;{problem_id}/Robot/ver&#x3D;{version}/'.format(problem_id=56, version=1.2),
                                    method='POST',
                                    data=json.dumps(robot),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_robot(self):
        """
        Test case for delete_robot

        Delete Robot
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/Robot/rid&#x3D;{robot_id}/ver&#x3D;{version}/'.format(problem_id=56, robot_id=56, version=1.2),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_robot(self):
        """
        Test case for get_robot

        Get a robot by the ID
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/Robot/rid&#x3D;{robot_id}'.format(problem_id=56, robot_id=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_robots(self):
        """
        Test case for get_robots

        Robot
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/Robot'.format(problem_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_robot(self):
        """
        Test case for update_robot

        Update the existing robot value
        """
        robot = Robot()
        response = self.client.open('/v2/id&#x3D;{problem_id}/Robot/rid&#x3D;{robot_id}/ver&#x3D;{version}/'.format(problem_id=56, version=1.2, robot_id=56),
                                    method='PUT',
                                    data=json.dumps(robot),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
