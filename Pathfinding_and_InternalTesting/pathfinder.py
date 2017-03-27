#!/usr/bin/python

import json
import math
from pprint import pprint
from latLongConversion import *



""" ROUND2 TEAM 2 ECE 4574 Instructions
    Adapted from Round 1 TEAM 5 code
    Video test: https://youtu.be/XuV_3L8GiAM
CALL pathfind_from_json(parsed_json) to run the program!
"""

""" --- A* Algorithim Module from pypaths ----
Adapted from pypaths, found at https://pypi.python.org/pypi/pypaths/0.1.2

The pathfinding module can be used to find the shortest
path between two points in a graph.

To use the pathfinder for the default case:
>>> finder = pathfinder()
>>> finder( (0,0), (1,1) )
(2, [(0, 0), (0, 1), (1, 1)])
Or, to customize the pathfinder via passed in functions to handle for your
particular graph implementation:
>>> finder = pathfinder( distance=absolute_distance,        \\
...                      cost=fixed_cost(2),                \\
...                      neighbors=grid_neighbors(10,10) );
>>> finder( (0,0), (2,2) )
(8, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)])
If a maximum cost is specified, then an empty path will be returned if
the cost exceeded the specified maximum
>>> finder( (0,0), (2,2), 7 )
(None, [])
"""

Global_scale = 5

#globally store JSON message
Json = json.loads('{}')

def update_json(json_message):
    global Json
    Json = json_message

def intersects_obstacle(c):
    #print(c)
    # we will look through all obstacles, and check if any intersect a point.
    # this boolean is then returned
    doesIntersect = False
    loc = 0
    #while loc < len(data["obstacles"][loc]["obstacle_info"]):

    #doesIntersect = (c[0] >= Json["obstacles"][loc]["obstacle_info"]["coordinates"]["x"]) and (c[0] <= Json["obstacles"][loc]["obstacle_info"]["coordinates"]["x"] + Json["obstacles"][loc]["obstacle_info"]["width"]) and (c[1] >= Json["obstacles"][loc]["obstacle_info"]["coordinates"]["y"]) and (c[1] <= Json["obstacles"][loc]["obstacle_info"]["coordinates"]["y"] + Json["obstacles"][loc]["obstacle_info"]["height"])
    #print("runs")
    #print("In Intersect obstacles x_min is {0}".format(Json["obstacles"][1]["obstacle_info"]["x_min"]))
    while doesIntersect is not False and loc < len(Json["obstacles"]):
        #doesIntersect = (c[0] >= Json["obstacles"][loc]["obstacle_info"]["x_min"]) and (c[0] <= Json["obstacles"][loc]["obstacle_info"]["x_min"] + Json["obstacles"][loc]["obstacle_info"]["width"]) and (c[1] >= Json["obstacles"][loc]["obstacle_info"]["y_min"]) and (c[1] <= Json["obstacles"][loc]["obstacle_info"]["y_min"] + Json["obstacles"][loc]["obstacle_info"]["height"])
        doesIntersect = (c[0] >= Json["obstacles"][loc]["obstacle_info"]["x_min"]) and (c[0] <= Json["obstacles"][loc]["obstacle_info"]["x_min"] + 5000) and (c[1] >= Json["obstacles"][loc]["obstacle_info"]["y_min"]) and (c[1] <= Json["obstacles"][loc]["obstacle_info"]["y_min"] + 5000)

        loc += 1
    #print(doesIntersect)
    return doesIntersect

# START ORIGINAL MODULE #########################################################
def manhattan_distance(start, end):
    """
    Calculate the manhattan distance between two points.
    >>> manhattan_distance( (0,0), (5,5) )
    10
    """
    dist = abs(start[0] - end[0]) + abs(start[1] + end[1])
    print("\nManhattan Distance: {0} \n\tSTART X= {1} , GOAL X= {2}\n\tSTART Y= {3} , GOAL Y= {4}".format(dist, start[0], end[0], start[1], end[1]))

    return dist


def absolute_distance(start, end):
    """
    Calculate the distance between two points using the distance formula.
    >>> absolute_distance( (1,2), (5,5) )
    5.0
    """
    dist = math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

    return dist


def latlongdistance(start, end):
    p = 0.017453292519943295
    a = 0.5 - cos((start[1] - start[0]) * p)/2 + cos(start[0] * p) * cos(start[1] * p) * (1 - cos((end[1] - end[0]) * p)) / 2

    dist = 12742 * asin(sqrt(a))
    print("\nLat Long Distance: {0} \n\tSTART X= {1} , GOAL X= {2}\n\tSTART Y= {3} , GOAL Y= {4}".format(dist, start[0], end[0], start[1], end[1]))
    return dist

def fixed_cost(cost):
    """
    Return a fixed cost for all coordinates in the graph.
    >>> cost = fixed_cost( 20 )
    >>> cost( 1, 2 )
    20
    >>> cost( 3, 4 )
    20
    """

    def func(a, b):
        return cost

    return func


def grid_neighbors(minx, miny, height, width):
    """
    Calculate neighbors for a simple grid where
    a movement can be made up, down, left, or right.
    Arguments:
    height - The height of the grid
    width - The width of the grid
    >>> neighbor = grid_neighbors( 10, 10 )
    >>> neighbor( (0,0) )
    [(0, 1), (1, 0)]
    >>> neighbor( (1,1) )
    [(1, 2), (1, 0), (2, 1), (0, 1)]
    """

    def func(coord):
        neighbor_list = [(coord[0], coord[1] + 1),
                         (coord[0], coord[1] - 1),
                         (coord[0] + 1, coord[1]),
                         (coord[0] - 1, coord[1])]
        #print("Grid Neighbors: {0}".format(neighbor_list))

        return [c for c in neighbor_list
                if c != coord
                and not intersects_obstacle(c)
                and c[0] >= minx and c[0] < width
                and c[1] >= miny and c[1] < height]

    return func


def pathfinder(neighbors=grid_neighbors(0, 0, 100, 100),
               distance=absolute_distance,
               cost=fixed_cost(1)):
    """
    Find the shortest distance between two nodes in a graph using the
    astar algorithm. By default, the graph is a coordinate plane where
    every node has the same cost and nodes can be traversed horizontally
    and vertically.
    Keyword Arguments:
    neighbor - Callable that takes a node and returns a list
               of neighboring nodes.
    distance - Callable that returns the estimated distance
               between two nodes.
    cost     - Callable that returns the cost to traverse
               between two given nodes.
    """

    def reconstruct_path(came_from, current_node):
        """Reconstruct the path from a given node to the beginning"""
        if current_node in came_from:
            p = reconstruct_path(came_from, came_from[current_node])
            p.append(current_node)
            return p
        else:
            return [current_node]

    def func(start, end, max_cost=None):
        """
        Perform a-star pathfinding from a start to an
        end coordinate.
        Returns a tuple containing the cost associated with
        the path, and a list of coordinates in the path
        This implementation is based on the wikipedia pseudocode, which
        translated almost directly into python.
        http://en.wikipedia.org/wiki/A*_search_algorithm
        """
        open_set = set([start])
        closed_set = set()
        came_from = {}

        g_score = {start: 0}
        f_score = {start: cost(start, end)}

        while len(open_set) != 0:
            current = min(open_set, key=lambda c: f_score[c])

            if max_cost != None and g_score[current] > max_cost:
                break

            if current == end:
                return g_score[current], reconstruct_path(came_from, end)

            open_set.discard(current)
            closed_set.add(current)
            for neighbor in neighbors(current):
                tentative_score = g_score[current] + cost(current, neighbor)

                if neighbor in closed_set and (neighbor in g_score and tentative_score >= g_score[neighbor]):
                    continue

                if neighbor not in open_set or (neighbor in g_score and tentative_score < g_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_score
                    f_score[neighbor] = tentative_score + distance(neighbor, end)

                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return None, []

    return func
# END ORIGINAL MODULE #########################################################

# enable is used for real world application. Set it to 1. Removex X,Y from final path output
# set to 0 if in debug/test mode as tests will require X,Y in final path output
def pathfind_from_json(json_message, enable):
    # Takes original JSON and high level converts it
    if enable == 1:
        conv_json = readJSON(json_message, Global_scale)
        update_json(conv_json)
    else:
        update_json(json_message)
    """
    print("Boundary is {0}, {1} of width {2} and height {3}".format(Json["boundary"]["boundary_info"]["x_min"],
     Json["boundary"]["boundary_info"]["y_min"], Json["boundary"]["boundary_info"]["width"], Json["boundary"]["boundary_info"]["height"]))
     """

    finder = pathfinder(distance=absolute_distance, cost=fixed_cost(1),
                        neighbors=grid_neighbors(Json["boundary"]["boundary_info"]["x_min"],
                         Json["boundary"]["boundary_info"]["y_min"],
                          Json["boundary"]["boundary_info"]["width"], Json["boundary"]["boundary_info"]["height"]))

    path = finder((Json["robots"][0]["coordinates"]["x"], Json["robots"][0]["coordinates"]["y"]), (Json["goal"]["coordinates"]["x"], Json["goal"]["coordinates"]["y"]))

    
    coordinate_array = []

    # Only write X,Y values into the output IF enable is set to 0 which means it is in debug/test mode. 
    for i, (x, y) in enumerate(path[1]):
        if enable == 1:
            temp_dict = { "latitude" : convert_y_to_lat(y), "longitude" : convert_x_to_lon(x)}
        else:
            temp_dict = { "latitude" : convert_y_to_lat(y), "longitude" : convert_x_to_lon(x),"x" : x, "y" : y}
        coordinate_array.append(temp_dict)

    path_dict = {  "path_cost" : path[0],
                   "coordinates": coordinate_array
                }
    if enable == 1:
        with open('pathout.json', 'w') as outfile:
            json.dump(path_dict, outfile, sort_keys = True, indent = 4, ensure_ascii = False)


    return path_dict # Returns JSON Object





