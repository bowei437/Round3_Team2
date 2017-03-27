import connexion
from werkzeug.exceptions import BadRequest
from swagger_server.models.error import Error
from swagger_server.models.obstacle import Obstacle
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://storage_container:8082/v2/"


def add_obstacle(problem_id, obstacle):
    """
    Add a new obstacle to the list
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle: Obstacle object that needs to be added to the list.
    :type obstacle: dict | bytes

    :rtype: int
    """

    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #check if input is JSON
    if connexion.request.is_json:
        #get JSON from input
        try:
            obstacle = Obstacle.from_dict(connexion.request.get_json())
        except (ValueError, BadRequest) as error:
            return jsonify(Error(400, "Validation error; please check inputs")), status.HTTP_400_BAD_REQUEST

        obstacle = connexion.request.get_json()

        #contact Storage
        params = "id=%s/" % str(problem_id)
        obst_url = storage_url + str(params)
        response = requests.get(obst_url)
     
        #check if Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't add Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #get Problem from response
        problem = response.json()["body"]
        version = response.json()["version"]

        #get Obstacles from Problem
        obstacles = problem["obstacles"]

        #make sure there isn't an Obstacle with the same ID
        if (not any(o_obstacle["obstacle_id"] == obstacle["obstacle_id"] for o_obstacle in obstacles)):
            obstacles.append(obstacle)
            problem["obstacles"] = obstacles
        else:
            return jsonify(Error(409, "Obstacle ID already exists; this must be a unique value")), status.HTTP_409_CONFLICT

        #PUT new Problem to Storage
        params = "id=%s/ver=%s/" % (str(problem_id), str(version))
        put_url = storage_url + str(params)
        put_response = requests.put(put_url, json=problem)

        #check if Storage died
        if (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't add Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        reply = {}
        reply["response"] = put_response.json()
        reply["version"] = problem["version"]
        #return response from Storage
        return jsonify(reply)
    
    #return error if not JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE



def delete_obstacle(problem_id, obstacle_id):
    """
    Delete Obstacle
    This removes the obstacle by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The ID of the Obstacle that needs to be deleted.
    :type obstacle_id: int

    :rtype: None
    """
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST
   
    #check if obstacle_id is positive
    if (obstacle_id < 0):
        return jsonify(Error(400, "Negative Obstacle_ID")), status.HTTP_400_BAD_REQUEST

    #contact Storage
    params = "id=%s/" % str(problem_id)
    obst_url = storage_url + str(problem_id)
    response = requests.get(obst_url)
    
    #check if Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't delete Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()["body"]
    version = response.json()["version"]

    #get obstacles from Problem
    obstacles = problem["obstacles"]


    #make sure there isn't an Obstacle with the same ID
    if (not any(o_obstacle["obstacle_id"] == obstacle_id for o_obstacle in obstacles)):
        return jsonify(Error(404, "Obstacle not found")), status.HTTP_404_NOT_FOUND
    else:
        for obstacle in obstacles:
            if (obstacle["obstacle_id"] == obstacle_id):
                obstacles.remove(obstacle)
        problem["obstacles"] = obstacles

    #PUT new Problem to Storage
    params = "id=%s/ver=%s/" % (str(problem_id), str(version))
    put_url = storage_url + str(params)
    put_response = requests.put(put_url, json=problem)

    #check if Storage died
    if (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't delete Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR


    #return response from Storage
    return jsonify({"response" : "Successfully deleted obstacle"})


def get_obstacle(problem_id, obstacle_id):
    """
    Obstacles
    Returns an obstacle 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The id of the obstacle to be updated.
    :type obstacle_id: int

    :rtype: Obstacle
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #check if obstacle_id is positive
    if (obstacle_id < 0):
        return jsonify(Error(400, "Negative Obstacle_ID")), status.HTTP_400_BAD_REQUEST

    #contact Storage
    obst_url = storage_url + str(problem_id)
    response = requests.get(obst_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't get Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()

    #get Obstacles from Problem
    obstacles = problem["obstacles"]

    #look through Robots for the one with a specific ID
    for obstacle in obstacles:
        if (obstacle["obstacle_id"] == obstacle_id):
            reply = {}
            reply["obstacle"] = obstacle
            reply["version"] = problem["version"]
            return jsonify(reply)

    #return error if not found
    return jsonify(Error(404, "Obstacle not found")), status.HTTP_404_NOT_FOUND


def get_obstacles(problem_id):
    """
    Obstacles
    Returns a list of all of the obstacles in the problem. This can be an empty list. 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: List[Obstacle]
    """
        #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #contact Storage
    obst_url = storage_url + str(problem_id)
    response = requests.get(obst_url)

    #check that Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't get Obstacles")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()

    #return the list of Obstacles
    reply = {}
    reply["obstacles"] = problem["obstacles"]
    return jsonify(reply)


def update_obstacle(problem_id, obstacle_id, updated_obstacle=None):
    """
    Update an existing obstacle
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The id of the obstacle to be updated.
    :type obstacle_id: int
    :param updated_obstacle: Obstacle object that needs to be added to the list.
    :type updated_obstacle: dict | bytes

    :rtype: None
    """
    updated_obstacle = Obstacle.from_dict(connexion.request.get_json())

    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #check if obstacle_id is positive
    if (obstacle_id < 0):
        return jsonify(Error(400, "Negative Obstacle_ID")), status.HTTP_400_BAD_REQUEST

    #check if input is JSON
    if connexion.request.is_json:
        #get JSON from input
        obstacle = connexion.request.get_json()

        try:
            obstacle = Obstacle.from_dict(connexion.request.get_json())
        except (ValueError, BadRequest) as error:
            return jsonify(Error(400, "Validation error; please check inputs")), status.HTTP_400_BAD_REQUEST
        #contact Storage
        params = "id=%s/" % str(problem_id)
        obst_url = storage_url + str(problem_id)
        response = requests.get(obst_url)
        
        #check if Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #get Problem from response
        problem = response.json()["body"]
        version = response.json()["version"]

        #get list of Obstacles from Problem
        obstacles = problem["obstacles"]

        #Go through list of Obstacles for a specific ID
        #if found, update coordinates and break loop
        changed = False;
        for o_obstacle in obstacles:
            if (o_obstacle["obstacle_id"] == obstacle_id):
                obstacles.remove(o_obstacle)
                obstacles.append(obstacle)
                problem["obstacles"] = obstacles
                changed = True
                break

        #if no Obstacle was found, return error
        if(not changed):
            return jsonify(Error(404, "Obstacle not found")), status.HTTP_404_NOT_FOUND

        #PUT new Problem into Storage
        params = "id=%s/ver=%s/" % (str(problem_id), str(version))
        put_url = storage_url + str(params)
        put_response = requests.put(put_url, json=problem)

        #check if Storage died
        if (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        return jsonify({"message" : "Successfully updated"})
    #return Error if not JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

