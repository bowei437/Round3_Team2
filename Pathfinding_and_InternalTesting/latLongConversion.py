import json
import math
from decimal import Decimal, ROUND_HALF_UP
# Here are all your options for rounding:
# This one offers the most out of the box control
# ROUND_05UP       ROUND_DOWN       ROUND_HALF_DOWN  ROUND_HALF_UP
# ROUND_CEILING    ROUND_FLOOR      ROUND_HALF_EVEN  ROUND_UP

# Function called by pathfind_from_json which takes the data it gets initially
# and does the primary conversion of data into the proper X, Y and lat long
def readJSON(data, scale):

    #globally store JSON message
    Json = json.loads('{}')

    #Boundary
    x = convert_lon_to_x(data["boundary"]["boundary_info"]["coordinates"][0]["longitude"])
    y = convert_lat_to_y(data["boundary"]["boundary_info"]["coordinates"][0]["latitude"])
    data["boundary"]["boundary_info"]["coordinates"][0]["x"] = x
    data["boundary"]["boundary_info"]["coordinates"][0]["y"] = y

    #Goal
    x = convert_lon_to_x(data["goal"]["coordinates"]["longitude"])
    y = convert_lat_to_y(data["goal"]["coordinates"]["latitude"])
    data["goal"]["coordinates"]["x"] = x
    data["goal"]["coordinates"]["y"] = y
    
    #Obstacles
    loc = 0
    loc2 = 0
    loc2tot = 0
    #print("length of obstacles: {0}\nObstacle1: {1}\n".format(len(data["obstacles"]), data["obstacles"][0]))
    #print(data["obstacles"][loc]["obstacle_info"]["name"])

    if "obstacles" not in data:
        print("No Obstacles")
    else:
            while loc < len(data["obstacles"]):
                while loc2 < len(data["obstacles"][loc]["obstacle_info"]["coordinates"]):
                    data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["x"] = convert_lon_to_x(data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["longitude"])
                    data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["y"] = convert_lat_to_y(data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["latitude"])
                    loc2 += 1
                if (data["obstacles"][loc]["obstacle_info"]["name"] == "rectangle"):
                    if (loc2 != 4):
                        print("WARNING: Obstacle at location {0} of shape rectangle does not have 4 points".format(loc))
                loc += 1
                loc2 = 0
    #print(loc2tot)
    #print(loc)
    loc = 0
    loc2 = 0
    # Calculates rectangular boundary width and height

    # Makes polygon into normalized rectangle
    while loc < len(data["obstacles"]):
        if (data["obstacles"][loc]["obstacle_info"]["name"] == "polygon"):
            print("\nPolygon at {0}".format(loc))
            polynum = len(data["obstacles"][loc]["obstacle_info"]["coordinates"])
            #print(polynum)
            #Temporary max min values
            Tx_max = max(data["obstacles"][loc]["obstacle_info"]["coordinates"], key=lambda ev: ev["x"])
            Ty_max = max(data["obstacles"][loc]["obstacle_info"]["coordinates"], key=lambda ev: ev["y"])
            Tx_min = min(data["obstacles"][loc]["obstacle_info"]["coordinates"], key=lambda ev: ev["x"])
            Ty_min = min(data["obstacles"][loc]["obstacle_info"]["coordinates"], key=lambda ev: ev["y"])
            # Store actual max min values
            x_max = Tx_max["x"]
            y_max = Ty_max["y"]
            x_min = Tx_min["x"]
            y_min = Ty_min["y"]
            print("\nx_max is {0} | y_max is {1}\nx_min is {2} | y_min is {3}".format(x_max, y_max, x_min, y_min))






        loc +=1

    #Robot
    x = convert_lon_to_x(data["robots"][0]["coordinates"]["longitude"])
    y = convert_lat_to_y(data["robots"][0]["coordinates"]["latitude"])
    data["robots"][0]["coordinates"]["x"] = x
    data["robots"][0]["coordinates"]["y"] = y
    
    # data.json is the name of the temporary output file that shows us what this file 'gives' back to
    # pathfinder. It is an intermediate json and should not be taken as what pathfinder actually outputs.
    # It is meant for debugging
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
    
    return data

# Pseudo Mercator Projections
# Please don't hate me for the conversion below. It was honestly the best way to do it.
# Round of float did not work. So it is rounded to decimal places by casting to string and recasting to float
def convert_lon_to_x(lon):
    r_major = 6378137.000
    string = "{:.3f}".format(r_major*math.radians(lon))
    temp = float(string)
    xout = round(temp, 1) 
    #print("LON TEMP: {0} | {1}".format(temp, xout)) 
    return xout

def convert_lat_to_y(lat):
    r_major = 6378137.000
    tmath = 0-r_major*math.log(math.tan(math.pi/4.0+lat*(math.pi/180.0)/2.0))
    string = "{:.3f}".format(tmath)
    temp = float(string) 
    yout = round(temp, 1)
    #print("LAT TEMP: {0} | {1}".format(temp, yout))

    return yout

def convert_x_to_lon(x):
    r_major = 6378137.000
    return math.degrees(x/r_major)

def convert_y_to_lat(y):
    r_major = 6378137.000
    y = (0-y)/r_major
    return 180.0/math.pi*(2.0*math.atan(math.exp(y))-math.pi/2.0)



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
