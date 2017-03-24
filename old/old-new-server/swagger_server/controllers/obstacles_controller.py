import connexion
from swagger_server.models.error import Error
from swagger_server.models.obstacle import Obstacle
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from flask import jsonify
from werkzeug.exceptions import BadRequest
from flask_api import status


def add_obstacle(problem_id, obstacle):
    """
    Add a new obstacle to the list
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle: Obstacle object that needs to be added to the list.
    :type obstacle: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        try:
            obstacle = Obstacle.from_dict(connexion.request.get_json())
        except BadRequest as e:
            #return jsonify({"error" : str(e)}), status.HTTP_400_BAD_REQUEST
            return str(e), 401
    return 'do some magic!'


def delete_obstacle(problem_id, obstacle_id):
    """
    Delete Obstacle
    This removes the obstacle by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The ID of the Obstacle that needs to be deleted.
    :type obstacle_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_obstacle(problem_id, obstacle_id):
    """
    Obstacles
    Returns an obstacle 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The id of the obstacle to be updated.
    :type obstacle_id: int

    :rtype: Obstacle
    """
    return 'do some magic!'


def get_obstacles(problem_id):
    """
    Obstacles
    Returns a list of all of the obstacles in the problem. This can be an empty list. 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: List[Obstacle]
    """
    return 'do some magic!'


def update_obstacle(problem_id, obstacle_id, updated_obstacle=None):
    """
    Update an existing obstacle
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The id of the obstacle to be updated.
    :type obstacle_id: int
    :param updated_obstacle: Obstacle object that needs to be added to the list.
    :type updated_obstacle: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        updated_obstacle = Obstacle.from_dict(connexion.request.get_json())
    return 'do some magic!'
