import connexion
from swagger_server.models.error import Error
from swagger_server.models.obstacle import Obstacle
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-52-41-229-1.us-west-2.compute.amazonaws.com:8080/v1/"


def add_obstacle(problem_id, version, obstacle):
    """
    Add a new obstacle to the list
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float
    :param obstacle: Obstacle object that needs to be added to the list.
    :type obstacle: dict | bytes

    :rtype: int
    """

    #check if input is JSON
    if connexion.request.is_json:
        #get JSON from input
        obstacle = connexion.request.get_json()

        #contact Storage
        obst_url = storage_url + str(problem_id)
        response = requests.get(obst_url)
     
        #check if Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't add Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #get Problem from response
        problem = response.json()

        #make sure versions match
        if (version != problem["version"]):
            return jsonify(Error(409, ("Versions numbers do not match. Version should be:" + str(problem['version'])))), status.HTTP_409_CONFLICT
        

        #############################################
        #   THIS IS WHERE I WOULD SANITIZE INPUTS   #
        #                                           #
        #     [INSERT TIMMY TURNER'S DAD MEME]      #
        #                                           #
        #   IF I HAD A WORKING SANITIZE FUNCTION    #
        #############################################


        #get Obstacles from Problem
        obstacles = problem["obstacles"]

        #make sure there isn't an Obstacle with the same ID
        if (not any(o_obstacle["obstacle_id"] == obstacle["obstacle_id"] for o_obstacle in obstacles)):
            obstacles.append(obstacle)
            problem["obstacles"] = obstacles
        else:
            return jsonify(Error(409, "Obstacle ID already exists; this must be a unique value")), status.HTTP_409_CONFLICT

        #update version number
        new_version = problem["version"]
        new_version = new_version + 1
        problem["version"] = new_version

        #PUT new Problem to Storage
        put_response = requests.put(obst_url, json=problem)

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



def delete_obstacle(problem_id, obstacle_id, version):
    """
    Delete Obstacle
    This removes the obstacle by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The ID of the Obstacle that needs to be deleted.
    :type obstacle_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float

    :rtype: None
    """
    #contact Storage
    obst_url = storage_url + str(problem_id)
    response = requests.get(obst_url)
    
    #check if Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't delete Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()

    #make sure versions match
    if (version != problem["version"]):
        return jsonify(Error(409, ("Versions numbers do not match. Version should be: " + str(problem['version'])))), status.HTTP_409_CONFLICT
    
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

    #update version number
    new_version = problem["version"]
    new_version = new_version + 1
    problem["version"] = new_version

    #PUT new Problem to Storage
    put_response = requests.put(obst_url, json=problem)

    #check if Storage died
    if (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't delete Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    reply = {}
    reply["response"] = put_response.json()
    reply["version"] = problem["version"]

    #return response from Storage
    return jsonify(reply)


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
    reply["version"] = problem["version"]
    return jsonify(reply)

def update_obstacle(problem_id, obstacle_id, version, updated_obstacle=None):
    """
    Update an existing obstacle
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param obstacle_id: The id of the obstacle to be updated.
    :type obstacle_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float
    :param updated_obstacle: Obstacle object that needs to be added to the list.
    :type updated_obstacle: dict | bytes

    :rtype: None
    """

    #check if input is JSON
    if connexion.request.is_json:
        #get JSON from input
        obstacle = connexion.request.get_json()

        #contact Storage
        obst_url = storage_url + str(problem_id)
        response = requests.get(obst_url)
        
        #check if Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update Obstacle")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #get Problem from response
        problem = response.json()

        #check if versions match
        if (version != problem["version"]):
            return jsonify(Error(409, ("Versions numbers do not match. Version should be: " + str(problem['version'])))), status.HTTP_409_CONFLICT
        
        #get list of Obstacles from Problem
        obstacles = problem["obstacles"]

        #Go through list of Obstacles for a specific ID
        #if found, update coordinates and break loop
        changed = False;
        for o_obstacle in obstacles:
            if (o_obstacle["obstacle_id"] == obstacle_id):

                #############################################
                #   THIS IS WHERE I WOULD SANITIZE INPUTS   #
                #                                           #
                #     [INSERT TIMMY TURNER'S DAD MEME]      #
                #                                           #
                #   IF I HAD A WORKING SANITIZE FUNCTION    #
                #############################################
                obstacles.remove(o_obstacle)
                obstacles.append(obstacle)
                problem["obstacles"] = obstacles
                changed = True
                break

        #if no Obstacle was found, return error
        if(not changed):
            return jsonify(Error(404, "Obstacle not found")), status.HTTP_404_NOT_FOUND

        #update version
        new_version = problem["version"]
        new_version = new_version + 1
        problem["version"] = new_version

        #PUT new Problem into Storage
        put_response = requests.put(obst_url, json=problem)

        #check if Storage died
        if (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
        

        #return response from Storage
        reply = {}
        reply["response"] = put_response.json()
        reply["version"] = problem["version"]
        return jsonify(reply)
    #return Error if not JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
