import connexion
from swagger_server.models.boundary import Boundary
from swagger_server.models.error import Error
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_boundary(problem_id):
    """
    Boundary
    Returns a description of the boundary
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Boundary
    """
    return 'do some magic!'


def update_boundary(problem_id, boundary):
    """
    Update the existing boundary value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param boundary: Boundary object that needs to be updated.
    :type boundary: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        boundary = Boundary.from_dict(connexion.request.get_json())
    return 'do some magic!'
