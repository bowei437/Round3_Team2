import connexion
from werkzeug.exceptions import BadRequest
from swagger_server.models.error import Error
from swagger_server.models.robot import Robot
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-35-167-218-237.us-west-2.compute.amazonaws.com:8000/v2/"

def add_robot(problem_id, robot):
    """
    Add a new robot to the list
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot: Obstacle object that needs to be added to the list.
    :type robot: dict | bytes

    :rtype: None
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #check that input is JSON
    if connexion.request.is_json:
        #get JSON from input
        try:
            robot = Robot.from_dict(connexion.request.get_json())
        except (ValueError, BadRequest) as error:
            return jsonify(Error(400, "Validation error; please check inputs")), status.HTTP_400_BAD_REQUEST

        robot = connexion.request.get_json()


        #Storage version control
        while True:
            #contact Storage
            params = "id=%s/" % str(problem_id)
            robot_url = storage_url + str(params)
            response = requests.get(robot_url)
     
            #check if Problem exists
            if (response.status_code == 404):
                return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
            #check if Storage died
            elif (response.status_code != 200):
                return jsonify(Error(500, "Storage server error: couldn't access Robots")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
            #get Problem from response
            problem = response.json()["body"]
            version = response.json()["version"]
   
            '''
            #check if robot is in valid range
            test_msg = sanitize_robot(robot, problem)
            if (test_msg is not "No Error"):
                return jsonify(Error(400, test_msg)), status.HTTP_400_BAD_REQUEST
            '''

            #get robots from Problem
            robots = problem["robots"]
  
            #make sure there isn't a Robot with the same ID
            if (not any(o_robot["id"] == robot["id"] for o_robot in robots)):
                robots.append(robot)
                problem["robots"] = robots
            else:
                return jsonify(Error(409, "Robot ID already exists; this must be a unique value")), status.HTTP_409_CONFLICT

            #PUT new Problem to Storage
            params = "id=%s/ver=%s/" % (str(problem_id), str(version))
            put_url = storage_url + str(params)
            put_response = requests.put(put_url, json=problem)

            #check for Storage version control
            if (response.status_code != 412):
                #check if Storage died
                if (response.status_code != 200):
                    return jsonify(Error(500, "Storage server error: couldn't add new robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
                break

        #return response
        return jsonify({"response":"update successful"})
    
    #return error if not JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE


def delete_robot(problem_id, robot_id):
    """
    Delete Robot
    This removes the robot by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot_id: The ID of the Obstacle that needs to be deleted.
    :type robot_id: int

    :rtype: None
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST
   
    #check if robot_id is positive
    if (robot_id < 0):
        return jsonify(Error(400, "Negative Robot_ID")), status.HTTP_400_BAD_REQUEST
   
    #Storage version control
    while True: 
        #contact Storage
        params = "id=%s/" % str(problem_id)
        robot_url = storage_url + str(params)
        response = requests.get(robot_url)
    
        #check if Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't access Robots")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
        #get Problem from response
        problem = response.json()["body"]
        version = response.json()["version"]

        #get robots from Problem
        robots = problem["robots"]

        if (len(robots) == 1):
            return jsonify(Error(400, "Must be at least 1 robot in problem")), status.HTTP_400_BAD_REQUEST

        #make sure there isn't a Robot with the same ID
        if (not any(o_robot["id"] == robot_id for o_robot in robots)):
            return jsonify(Error(404, "Robot not found")), status.HTTP_404_NOT_FOUND
        else:
            for robot in robots:
                if (robot["id"] == robot_id):
                    robots.remove(robot)
            problem["robots"] = robots

        #PUT new Problem to Storage
        params = "id=%s/ver=%s/" % (str(problem_id), str(version))
        put_url = storage_url + params
        put_response = requests.put(put_url, json=problem)
  
        #check for Storage version control
        if (put_response.status_code != 412):
            #check if Storage died
            if (put_response.status_code != 200):
                return jsonify(Error(500, "Storage server error: couldn't add new robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
            break

    #return response from Storage
    return jsonify({"response":"delete successful"})


def get_robot(problem_id, robot_id):
    """
    Get a robot by the ID
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot_id: Robot object that needs to be updated.
    :type robot_id: int

    :rtype: Robot
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #check if robot_id is positive
    if (robot_id < 0):
        return jsonify(Error(400, "Negative Robot_ID")), status.HTTP_400_BAD_REQUEST

    #contact Storage
    params = "id=%s/" % str(problem_id)
    robot_url = storage_url + str(params)
    response = requests.get(robot_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't access Robots")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()["body"]

    #get Robots from Problem
    robots = problem["robots"]

    #look through Robots for the one with a specific ID
    for robot in robots:
        if (robot["id"] == robot_id):
            reply = {}
            reply["robot"] = robot
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
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #contact Storage
    params = "id=%s/" % str(problem_id)
    robot_url = storage_url + str(params)
    response = requests.get(robot_url)

    #check that Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error: couldn't get Robots")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get Problem from response
    problem = response.json()["body"]

    #return the list of Robots
    reply = {}
    reply["robots"] = problem["robots"]
    return jsonify(reply)


def update_robot(problem_id, robot, robot_id):
    """
    Update the existing robot value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param robot: Robot object that needs to be updated.
    :type robot: dict | bytes
    :param robot_id: Robot object that needs to be updated.
    :type robot_id: int

    :rtype: None
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    #check if robot_id is positive
    if (robot_id < 0):
        return jsonify(Error(400, "Negative Robot_ID")), status.HTTP_400_BAD_REQUEST

    #check if input is JSON
    if connexion.request.is_json:
        #get JSON from input
        try:
            robot = Robot.from_dict(connexion.request.get_json())
        except (ValueError, BadRequest) as error:
            return jsonify(Error(400, "Validation error; please check inputs")), status.HTTP_400_BAD_REQUEST
        robot = connexion.request.get_json()


        ''' 
        #check if robot is in valid range
        test_msg = sanitize_robot(robot)
            return jsonify(Error(400, test_msg)), status.HTTP_400_BAD_REQUEST
        '''
        #Storage version control
        while True:
            #contact Storage
            params = "id=%s/" % str(problem_id)
            robot_url = storage_url + str(params)
            response = requests.get(robot_url)
        
            #check if Problem exists
            if (response.status_code == 404):
                return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
            #check if Storage died
            elif (response.status_code != 200):
               return jsonify(Error(500, "Storage server error: couldn't update robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
            #get Problem from response
            problem = response.json()["body"]
            version = response.json()["version"]
     
            #get list of Robots from Problem
            robots = problem["robots"]

            #Go through list of Robots for a specific ID
            #if found, update coordinates and break loop
            changed = False;
            for o_robot in robots:
                if (o_robot["id"] == robot_id):

                    o_robot["coordinates"] = robot["coordinates"]
                    problem["robots"] = robots
                    changed = True
                    break

            #if no Robot was found, return error
            if(not changed):
                return jsonify(Error(404, "Robot not found")), status.HTTP_404_NOT_FOUND

            #PUT new Problem into Storage
            params = "id=%s/ver=%s/" % (str(problem_id), str(version))
            put_url = storage_url + str(params)
            put_response = requests.put(put_url, json=problem)
      
            #check for Storage version control
            if (response.status_code != 412):  
                #check if Storage died
                if (response.status_code != 200):
                    return jsonify(Error(500, "Storage server error: couldn't update robot")), status.HTTP_500_INTERNAL_SERVER_ERROR
                break
    
        #return response from Storage
        return jsonify({"response":"update successful"})

    #return Error if not JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE