import connexion
from swagger_server.models.error import Error
from swagger_server.models.robot import Robot
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-35-167-218-237.us-west-2.compute.amazonaws.com:8080/v1/"


def add_robot(problem_id, version, robot):
    """
    Add a new robot to the list
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float
    :param robot: Obstacle object that needs to be added to the list.
    :type robot: dict | bytes

    :rtype: int
    """
    #check that input is JSON
    if connexion.request.is_json:
        #get JSON from input
        robot = connexion.request.get_json()

        #contact Storage
        robot_url = storage_url + str(problem_id)
        response = requests.get(robot_url)
     
        #check if Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update Robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
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


        #get robots from Problem
        robots = problem["robots"]

        #make sure there isn't a Robot with the same ID
        if (not any(o_robot["id"] == robot["id"] for o_robot in robots)):
            robots.append(robot)
            problem["robots"] = robots
        else:
            return jsonify(Error(409, "Robot ID already exists; this must be a unique value")), status.HTTP_409_CONFLICT

        #update version number
        new_version = problem["version"]
        new_version = new_version + 1
        problem["version"] = new_version

        #PUT new Problem to Storage
        put_response = requests.put(robot_url, json=problem)

        #check if Storage died
        if (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't add new robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #return response from Storage
        reply = {}
        reply["robot"] = robot
        reply["version"] = problem["version"]
        return jsonify(reply)
    
    #return error if not JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE



def delete_robot(problem_id, robot_id, version):
    """
    Delete Robot
    This removes the robot by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot_id: The ID of the Obstacle that needs to be deleted.
    :type robot_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float

    :rtype: None
    """

    #contact Storage
    robot_url = storage_url + str(problem_id)
    response = requests.get(robot_url)
    
    #check if Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't update Robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()

    #make sure versions match
    if (version != problem["version"]):
        return jsonify(Error(409, ("Versions numbers do not match. Version should be %s", str(problem['version'])))), status.HTTP_409_CONFLICT
    
    #get robots from Problem
    robots = problem["robots"]

    #make sure there isn't a Robot with the same ID
    if (not any(o_robot["id"] == robot_id for o_robot in robots)):
        return jsonify(Error(404, "Robot not found")), status.HTTP_404_NOT_FOUND
    else:
        for robot in robots:
            if (robot["id"] == robot_id):
                robots.remove(robot)
        problem["robots"] = robots

    #update version number
    new_version = problem["version"]
    new_version = new_version + 1
    problem["version"] = new_version

    #PUT new Problem to Storage
    put_response = requests.put(robot_url, json=problem)

    #check if Storage died
    if (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't add new robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #return response from Storage
    reply = {}
    reply["version"] = problem["version"]
    reply["response"] = put_response.json()
    return jsonify(reply)


def get_robot(problem_id, robot_id):
    """
    Get a robot by the ID
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot_id: Robot object that needs to be updated.
    :type robot_id: int

    :rtype: Robot
    """

    #contact Storage
    robot_url = storage_url + str(problem_id)
    response = requests.get(robot_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't get Robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()

    #get Robots from Problem
    robots = problem["robots"]

    #look through Robots for the one with a specific ID
    for robot in robots:
        if (robot["id"] == robot_id):
            reply = {}
            reply["robot"] = robot
            reply["version"] = problem["version"]
            return jsonify(reply)

    #return error if not found
    return jsonify(Error(404, "Robot not found")), status.HTTP_404_NOT_FOUND
    

def get_robots(problem_id):
    """
    Robot
    Returns a description of the robots, including the current location 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: List[Robot]
    """

    #contact Storage
    robot_url = storage_url + str(problem_id)
    response = requests.get(robot_url)

    #check that Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't get Robots")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()

    #return the list of Robots
    reply = {}
    reply["robots"] = problem["robots"]
    reply["version"] = problem["version"]
    return jsonify(reply)


def update_robot(problem_id, version, robot, robot_id):
    """
    Update the existing robot value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float
    :param robot: Robot object that needs to be updated.
    :type robot: dict | bytes
    :param robot_id: Robot object that needs to be updated.
    :type robot_id: int

    :rtype: None
    """

    #check if input is JSON
    if connexion.request.is_json:
        #get JSON from input
        robot = connexion.request.get_json()

        #contact Storage
        robot_url = storage_url + str(problem_id)
        response = requests.get(robot_url)
        
        #check if Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #get Problem from response
        problem = response.json()

        #check if versions match
        if (version != problem["version"]):
            return jsonify(Error(409, ("Versions numbers do not match. Version should be: " + str(problem['version'])))), status.HTTP_409_CONFLICT
        
        #get list of Robots from Problem
        robots = problem["robots"]

        #Go through list of Robots for a specific ID
        #if found, update coordinates and break loop
        changed = False;
        for o_robot in robots:
            if (o_robot["id"] == robot_id):

                #############################################
                #   THIS IS WHERE I WOULD SANITIZE INPUTS   #
                #                                           #
                #     [INSERT TIMMY TURNER'S DAD MEME]      #
                #                                           #
                #   IF I HAD A WORKING SANITIZE FUNCTION    #
                #############################################

                o_robot["coordinates"] = robot["coordinates"]
                problem["robots"] = robots
                changed = True
                break

        #if no Robot was found, return error
        if(not changed):
            return jsonify(Error(404, "Robot not found")), status.HTTP_404_NOT_FOUND

        #update version
        new_version = problem["version"]
        new_version = new_version + 1
        problem["version"] = new_version

        #PUT new Problem into Storage
        put_response = requests.put(robot_url, json=problem)

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

