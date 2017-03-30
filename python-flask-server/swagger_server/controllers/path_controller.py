import connexion
from swagger_server.models.error import Error
from swagger_server.models.path import Path
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status
from pathfinder import *

storage_url = "http://ec2-54-149-42-191.us-west-2.compute.amazonaws.com:8000/v2/"

def get_path(problem_id):
    """
    Path
    Returns a description of the path from the robot&#39;s current location to the goal.
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Path
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #Storage version control   
    while True: 
        #contact storage
        params = "id=%s/" % str(problem_id)
        path_url = storage_url + str(params)
        response = requests.get(path_url)

        #check that the Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
        #get the Problem from the response
        problem = response.json()["body"]
        version = response.json()["version"]
        try:
            path = pathfind_from_json(problem, 1)
        except (ValueError, TypeError) as error:
            return jsonify(Error(400, "Incorrect problem structure: please check default problem", str(error))), status.HTTP_400_BAD_REQUEST
            
        problem["path"] = path

        params = "id=%s/ver=%s/" % (str(problem_id), str(version))
        put_url = storage_url + str(params)
        response = requests.put(put_url, json=problem)

        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
       
        #check for Storage version control
        if (response.status_code != 412):
            #check if Storage died
            if (response.status_code != 200):
                return jsonify(Error(500, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
            break

    return jsonify(path)

