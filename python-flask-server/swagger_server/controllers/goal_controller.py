import connexion
from werkzeug.exceptions import BadRequest
from swagger_server.models.error import Error
from swagger_server.models.goal import Goal
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-35-167-218-237.us-west-2.compute.amazonaws.com:8000/v2/"

def get_goal(problem_id):
    """
    Goal Location
    Returns a description of the goal location. 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Goal
    """
    #check if problem_id is nonnegative
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST
 
    #contact storage
    params = "id=%s/" % str(problem_id)
    goal_url = storage_url + str(params)
    response = requests.get(goal_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get the Problem from the response
    problem = response.json()["body"]

    reply = {}
    reply["goal"] = problem["goal"]

    #return the Goal from the Problem
    return jsonify(reply)


def update_goal(problem_id, goal):
    """
    Update the existing goal value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param goal: Goal object that needs to be updated.
    :type goal: dict | bytes

    :rtype: None
    """
    #check if problem_id is positive 
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    if connexion.request.is_json:
        #check for input validity
        try:
            goal = Goal.from_dict(connexion.request.get_json())
        except (ValueError, BadRequest) as error:
            return jsonify(Error(400, "Validation error; please check inputs", str(error))), status.HTTP_400_BAD_REQUEST
        
        goal = connexion.request.get_json()

        #Storage version control
        while True:
            #contact Storage
            params = "id=%s/" % str(problem_id)
            goal_url = storage_url + str(params)
            response = requests.get(goal_url)
     
            #check that Problem exists
            if (response.status_code == 404):
                return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
            #check if Storage died
            elif (response.status_code != 200):
                return jsonify(Error(500, "Storage server error: couldn't update goal")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
            #get problem from response
            problem = response.json()["body"]
            version = response.json()["version"]
          
            #check if start and goal are in valid range
            #if (abs(problem['goal']['coordinates']['latitude'] -  ) > 100):
            #    return jsonify(Error(405, "Goal is out of range.")), HTTP_405_INVALID_INPUT

            #store new Goal coordinates into Goal of Problem

            problem['goal']['coordinates'] = goal['coordinates']
            #PUT the new Problem back into Storage
            params = "id=%s/ver=%s/" % (str(problem_id), str(version))
            goal_url = storage_url + str(params)
            put_response = requests.put(goal_url, json=problem)
      
            #check for Storage version control
            if (response.status_code != 412):
                #check if Storage died
                if (response.status_code != 200):
                    return jsonify(Error(500, "Storage server error: couldn't update goal")), status.HTTP_500_INTERNAL_SERVER_ERROR
                break
        
        return jsonify({"response":"Update successful"})

    #return an error if input isn't JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

