# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.obstacle import Obstacle
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestObstaclesController(BaseTestCase):
    """ ObstaclesController integration test stubs """

    def test_add_obstacle(self):
        """
        Test case for add_obstacle

        Add a new obstacle to the list
        """
        obstacle = Obstacle()
        response = self.client.open('/v3/id&#x3D;{problem_id}/Obstacles'.format(problem_id=56),
                                    method='POST',
                                    data=json.dumps(obstacle),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_obstacle(self):
        """
        Test case for delete_obstacle

        Delete Obstacle
        """
        response = self.client.open('/v3/id&#x3D;{problem_id}/Obstacles/obstacle_id&#x3D;{obstacle_id}'.format(problem_id=56, obstacle_id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_obstacle(self):
        """
        Test case for get_obstacle

        Obstacles
        """
        response = self.client.open('/v3/id&#x3D;{problem_id}/Obstacles/obstacle_id&#x3D;{obstacle_id}'.format(problem_id=56, obstacle_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_obstacles(self):
        """
        Test case for get_obstacles

        Obstacles
        """
        response = self.client.open('/v3/id&#x3D;{problem_id}/Obstacles'.format(problem_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_obstacle(self):
        """
        Test case for update_obstacle

        Update an existing obstacle
        """
        updated_obstacle = Obstacle()
        response = self.client.open('/v3/id&#x3D;{problem_id}/Obstacles/obstacle_id&#x3D;{obstacle_id}'.format(problem_id=56, obstacle_id=56),
                                    method='PUT',
                                    data=json.dumps(updated_obstacle),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
