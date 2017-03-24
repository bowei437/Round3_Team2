import connexion
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_problem():
    """
    Creates a new problem and returns a problemID
    

    :rtype: int
    """
    return 'do some magic!'


def delete_problem(problem_id):
    """
    Delete Problem
    This removes the problem by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_problem(problem_id):
    """
    Problems
    Returns a specific problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """
    return 'do some magic!'
