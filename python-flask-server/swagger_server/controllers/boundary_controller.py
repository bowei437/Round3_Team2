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
        #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #contact storage
    params = "id=%s/" % str(problem_id)
    bound_url = storage_url + str(params)
    response = requests.get(bound_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get the Problem from the response
    problem = response.json()["body"]

    #return the Boundary from the Problem
    return jsonify(problem["boundary"])


def update_boundary(problem_id, boundary):
    """
    Update the existing boundary value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param boundary: Boundary object that needs to be updated.
    :type boundary: dict | bytes

    :rtype: None
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    if connexion.request.is_json:
        #get JSON from response
        boundary = connexion.request.get_json()

        '''
        #check if boundary is in valid range
        test_msg = sanitize_boundary(boundary)
        if (test_msg is not "No error"):
            return jsonify(Error(400, test_msg)), status.HTTP_400_BAD_REQUEST
        '''

        #Storage version control
        while True:
            #contact Storage
            params = "id=%s/" % str(problem_id)
            bound_url = storage_url + str(params)
            response = requests.get(bound_url)
 
            #check that Problem exists
            if (response.status_code == 404):
                return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
            #check if Storage died
            elif (response.status_code != 200):
                return jsonify(Error(500, "Storage server error: couldn't access Boundary")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
            #get problem from response
            problem = response.json()['body']
            version = response.json()['version']

            #store new Goal coordinates into Goal of Problem
            problem['boundary'] = boundary

            #PUT the new Problem back into Storage
            params = "id=%s/ver=%s/" % (str(problem_id), str(version))
            put_url = storage_url + str(params)
            put_response = requests.put(put_url, json=problem)

            #check for Storage version control
            if (response.status_code != 412):
                #check if Storage died
                if (response.status_code != 200):
                    return jsonify(Error(500, "Storage server error: couldn't update goal")), status.HTTP_500_INTERNAL_SERVER_ERROR
                break
        
        #return the Boundary from the Problem
        return jsonify({"response": "update successful"})

    #return an error if input isn't JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
