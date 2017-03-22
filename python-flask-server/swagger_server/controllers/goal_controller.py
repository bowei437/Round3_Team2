import connexion
from swagger_server.models.error import Error
from swagger_server.models.goal import Goal
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_goal(problem_id):
    """
    Goal Location
    Returns a description of the goal location. 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Goal
    """
    return 'do some magic!'


def update_goal(problem_id, goal):
    """
    Update the existing goal value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param goal: Goal object that needs to be updated.
    :type goal: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        goal = Goal.from_dict(connexion.request.get_json())
    return 'do some magic!'
