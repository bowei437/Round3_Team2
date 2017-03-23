import connexion
from swagger_server.models.boundary import Boundary
from swagger_server.models.error import Error
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-35-167-218-237.us-west-2.compute.amazonaws.com:8000/v2/"


def get_boundary(problem_id):
    """
    Boundary
    Returns a description of the boundary
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Boundary
    """
        #contact storage
    bound_url = storage_url + str(problem_id)
    response = requests.get(bound_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get the Problem from the response
    problem = response.json()

    reply = {}
    reply["boundary"] = problem["boundary"]
    reply["version"] = problem["version"]
    #return the Boundary from the Problem
    return jsonify(reply)


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
