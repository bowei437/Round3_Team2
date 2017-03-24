import connexion
from swagger_server.models.error import Error
from swagger_server.models.robot import Robot
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_robot(problem_id, robot):
    """
    Add a new robot to the list
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot: Obstacle object that needs to be added to the list.
    :type robot: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        robot = Robot.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_robot(problem_id, robot_id):
    """
    Delete Robot
    This removes the robot by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot_id: The ID of the Obstacle that needs to be deleted.
    :type robot_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_robot(problem_id, robot_id):
    """
    Get a robot by the ID
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot_id: Robot object that needs to be updated.
    :type robot_id: int

    :rtype: Robot
    """
    return 'do some magic!'


def get_robots(problem_id):
    """
    Robot
    Returns a description of the robots, including the current location 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: List[Robot]
    """
    return 'do some magic!'


def update_robot(problem_id, robot, robot_id):
    """
    Update the existing robot value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot: Robot object that needs to be updated.
    :type robot: dict | bytes
    :param robot_id: Robot object that needs to be updated.
    :type robot_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        robot = Robot.from_dict(connexion.request.get_json())
    return 'do some magic!'
