import connexion
from swagger_server.models.error import Error
from swagger_server.models.path import Path
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_path(problem_id):
    """
    Path
    Returns a description of the path from the robot&#39;s current location to the goal.
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Path
    """
    return 'do some magic!'
