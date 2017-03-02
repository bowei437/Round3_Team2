import connexion
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-52-41-229-1.us-west-2.compute.amazonaws.com:8080/v1/"

"""
    This is the default Problem JSON. It needs to be updated
    as changes are made to API. The default from Swagger can 
    be found in the UI, under Problem - GET
"""
default_problem = {
"boundary": {
    "boundary_info": [
      {
        "latitude": 0,
        "longitude": 0
      }
    ]
  },
  "goal": {
    "coordinates": {
      "latitude": 0,
      "longitude": 0
    }
  },
  "obstacles": [
    {
      "obstacle_id": 0,
      "obstacle_info": [
        {
          "latitude": 0,
          "longitude": 0
        }
      ]
    }
  ],
  "problem_id": 0,
  "robots": [
    {
      "coordinates": {
        "latitude": 0,
        "longitude": 0
      },
      "id": 0
    }
  ],
  "version": 0
}
def add_problem():
    """
    Creates a new problem and returns a problemID
    

    :rtype: int
    """
    #contact storage server
    response = requests.post(storage_url)

    #check if storage comes back okay
    if (response.status_code != 200):
        return jsonify(Error(500, "Error in storage")), HTTP_500_INTERNAL_SERVER_ERROR
    
    #retrieve the uid
    json_response = response.json()
    uid = json_response['uid']
    
    #PUT the default Problem JSON into storage
    put_url = storage_url + str(uid)
    default_problem['uid'] = uid
    default_problem['problem_id'] = uid
    response = requests.put(put_url, json=default_problem)

    #check if the Problem does exist (It should, but its just for safety's sake)
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    #check that Storage didn't die in some way
    elif (response.status_code != 200):
        return jsonify(Error(response.status_code, response.text)), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #return the default problem so the user knows it has been created
    return jsonify(default_problem)


def delete_problem(problem_id, version):
    """
    Delete Problem
    This removes the problem by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float

    :rtype: None
    """

    #contact Storage
    url = storage_url + str(problem_id)
    get_response = requests.get(url)

    #make sure Problem existed
    if (get_response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if the Storage died
    elif (get_response.status_code != 200):
        return jsonify(Error(response.status_code, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #check that the version is correct
    problem = get_response.json()
    curr = problem["version"]
    if (curr != version):
        return jsonify(Error(409, "Versions do not match. Current version is " + str(curr))), status.HTTP_409_CONFLICT
    
    #try to DELETE Problem
    response = requests.delete(url)

    #check if the Storage died
    if (response.status_code != 200):
        return jsonify(Error(response.status_code, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #return response from Storage
    return jsonify(response.json())


def get_problem(problem_id):
    """
    Problems
    Returns a specific problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """
    
    #contact Storage
    get_url = storage_url + str(problem_id)
    response = requests.get(get_url)

    #make sure Problem existed
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(response.status_code, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    #return response from Storage
    return jsonify(response.json())
