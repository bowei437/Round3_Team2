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

storage_url = "http://ec2-52-41-229-1.us-west-2.compute.amazonaws.com:8080/v1/"


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


def update_boundary(problem_id, version, boundary):
    """
    Update the existing boundary value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float
    :param boundary: Boundary object that needs to be updated.
    :type boundary: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        #get JSON from response
        boundary = connexion.request.get_json()

        #contact Storage
        bound_url = storage_url + str(problem_id)
        response = requests.get(bound_url)
     
        #check that Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update boundary")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #get problem from response
        problem = response.json()

        #check that versions are the same
        if (version != problem["version"]):
            message = "Versions numbers do not match. Version should be: " + str(problem["version"])
            return jsonify(Error(409, message)), status.HTTP_409_CONFLICT
        

        #############################################
        #   THIS IS WHERE I WOULD SANITIZE INPUTS   #
        #                                           #
        #     [INSERT TIMMY TURNER'S DAD MEME]      #
        #                                           #
        #   IF I HAD A WORKING SANITIZE FUNCTION    #
        #############################################

        #store new Goal coordinates into Goal of Problem
        problem['boundary'] = boundary

        #update version - incrementing by 0.1 for now because it makes sense
        new_version = problem["version"]
        new_version = new_version + 1
        problem["version"] = new_version

        #PUT the new Problem back into Storage
        put_response = requests.put(bound_url, json=problem)
        
        #check if Storage died
        if (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update goal")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        reply = {}
        reply["response"] = put_response.json()
        reply["version"] = problem["version"]
        #return the Boundary from the Problem
        return jsonify(reply)

    #return an error if input isn't JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
