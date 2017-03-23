import json
import math

# Function called by pathfind_from_json which takes the data it gets initially
# and does the primary conversion of data into the proper X, Y and lat long
def readJSON(data, scale):

    #globally store JSON message
    Json = json.loads('{}')

    #Boundary
    x = convert_lon_to_x(data["boundary"]["boundary_info"][0]["latitude"])
    y = convert_lat_to_y(data["boundary"]["boundary_info"][0]["longitude"])
    data["boundary"]["boundary_info"][0]["x"] = x
    data["boundary"]["boundary_info"][0]["y"] = y

    #Goal
    x = convert_lon_to_x(data["goal"]["coordinates"]["latitude"])
    y = convert_lat_to_y(data["goal"]["coordinates"]["longitude"])
    data["goal"]["coordinates"]["x"] = x
    data["goal"]["coordinates"]["y"] = y

    #Obstacles
    loc = 0
    #print("length of obstacles: {0}\nObstacle1: {1}\n".format(len(data["obstacles"]), data["obstacles"][0]))

    if "obstacles" not in data:
        print("No Obstacles")
    else:
            while loc < len(data["obstacles"]):
                data["obstacles"][loc]["obstacle_info"][0]["x"] = convert_lon_to_x(data["obstacles"][loc]["obstacle_info"][0]["latitude"])
                data["obstacles"][loc]["obstacle_info"][0]["y"] = convert_lat_to_y(data["obstacles"][loc]["obstacle_info"][0]["longitude"])
                loc += 1

    #Robot
    x = convert_lon_to_x(data["robots"][0]["coordinates"]["latitude"])
    y = convert_lat_to_y(data["robots"][0]["coordinates"]["longitude"])
    data["robots"][0]["coordinates"]["x"] = x
    data["robots"][0]["coordinates"]["y"] = y
    
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
    
    return data

# Pseudo Mercator Projections
def convert_lon_to_x(lon):
    r_major = 6378137.000
    return r_major*math.radians(lon)

def convert_x_to_lon(x):
    r_major = 6378137.000
    return math.degrees(x/r_major)

def convert_y_to_lat(y):
    r_major = 6378137.000
    y = (0-y)/r_major
    return 180.0/math.pi*(2.0*math.atan(math.exp(y))-math.pi/2.0)

def convert_lat_to_y(lat):
    r_major = 6378137.000
    return 0-r_major*math.log(math.tan(math.pi/4.0+lat*(math.pi/180.0)/2.0))

# returns distance in meters on the mercator map projection
# from 0 lat 0 lon to the point on the sphere
def latlon_xy(coordinates):
    xy = []
    for coordinate in coordinates:
        # reversing order since lat comes first in these
        xy.append((convert_lon_to_x(coordinate[1]), convert_lat_to_y(coordinate[0])))
    return xy

def xy_latlon(points):
    coordinates = []
    for point in points:
        # reversing order since lat comes first in these
        coordinates.append((convert_y_to_lat(point[1]), convert_x_to_lon(point[0])))
    return coordinates

# Some other helpful functions
def findBoundingRectangle(coordinates):
    min_x = min(coordinates, key=lambda t: t[0])[0]
    min_y = min(coordinates, key=lambda t: t[1])[1]
    max_x = max(coordinates, key=lambda t: t[0])[0]
    max_y = max(coordinates, key=lambda t: t[1])[1]
    return [(min_x, min_y), (max_x, max_y)]

# rounds to nearest base
# ex. round(3.1415,10) => 0
# ex. round(3.1415,1) => 3
def round(x,base):
    return int(math.ceil(x/base))*base

def localizeXY(points,core):
    res = []
    for point in points:
        res.append( (point[0]-core[0],point[1]-core[1]) )
    return res

def rescaleXY(points,scale,base):
    res = []
    for point in points:
        res.append( (round(point[0]*scale,base),round(point[1]*scale,base)) )
    return res

def backscaleXY(points,scale):
    res = []
    for point in points:
        res.append( (round(point[0]/scale,1),round(point[1]/scale,1)) )
    return res

def delocalizeXY(points,core):
    res = []
    for point in points:
        res.append( (point[0]+core[0],point[1]+core[1]) )
    return res
