import json
import math
import utm
from decimal import Decimal, ROUND_HALF_UP
import sys
#print(sys.path)
# Here are all your options for rounding:
# This one offers the most out of the box control
# ROUND_05UP       ROUND_DOWN       ROUND_HALF_DOWN  ROUND_HALF_UP
# ROUND_CEILING    ROUND_FLOOR      ROUND_HALF_EVEN  ROUND_UP

# Function called by pathfind_from_json which takes the data it gets initially
# and does the primary conversion of data into the proper X, Y and lat long
def readJSON(data, scale):

    #globally store JSON message
    #print(sys.path)

    Json = json.loads('{}')
    loc = 0
    loc2 = 0
    """
    UTM Module Syntax:

    1: The syntax is utm.from_latlon(LATITUDE, LONGITUDE).
        The return has the form (EASTING, NORTHING, ZONE NUMBER, ZONE LETTER).

    2: The syntax is utm.to_latlon(EASTING, NORTHING, ZONE NUMBER, ZONE LETTER).
        The return has the form (LATITUDE, LONGITUDE).
    """

    #Boundary
    while loc < len(data["boundary"]["boundary_info"]["coordinates"]):
        cmerc = utm.from_latlon(data["boundary"]["boundary_info"]["coordinates"][loc]["latitude"], data["boundary"]["boundary_info"]["coordinates"][loc]["longitude"])
        # X is getting the Easting UTM value rounded to a whole number
        x = round(cmerc[0], 1)
        # Y is getting the Northing UTM value rounded to a whole number
        y = round(cmerc[1], 1)
        data["boundary"]["boundary_info"]["coordinates"][loc]["x"] = x
        data["boundary"]["boundary_info"]["coordinates"][loc]["y"] = y
        # Store the Zone Number and Zone LEtter as an additional intermediate variable used for conversoin back later
        data["boundary"]["boundary_info"]["coordinates"][loc]["zoneN"] = cmerc[2]
        data["boundary"]["boundary_info"]["coordinates"][loc]["zoneL"] = cmerc[3]

        loc += 1

    loc = 0
    while loc < len(data["boundary"]["boundary_info"]["coordinates"]):
        Tx_max = max(data["boundary"]["boundary_info"]["coordinates"], key=lambda ev: ev["x"])
        Ty_max = max(data["boundary"]["boundary_info"]["coordinates"], key=lambda ev: ev["y"])
        Tx_min = min(data["boundary"]["boundary_info"]["coordinates"], key=lambda ev: ev["x"])
        Ty_min = min(data["boundary"]["boundary_info"]["coordinates"], key=lambda ev: ev["y"])

        x_max = Tx_max["x"]
        y_max = Ty_max["y"]
        x_min = Tx_min["x"]
        y_min = Ty_min["y"]

        data["boundary"]["boundary_info"]["x_max"] = x_max
        data["boundary"]["boundary_info"]["y_max"] = y_max
        data["boundary"]["boundary_info"]["x_min"] = x_min
        data["boundary"]["boundary_info"]["y_min"] = y_min

        data["boundary"]["boundary_info"]["width"] = x_max - x_min
        data["boundary"]["boundary_info"]["height"] = y_max - y_min
        loc += 1


    #Goal
    cmerc = utm.from_latlon(data["goal"]["coordinates"]["latitude"], data["goal"]["coordinates"]["longitude"])
    x = round(cmerc[0], 1)
    y = round(cmerc[1], 1)
    data["goal"]["coordinates"]["x"] = x
    data["goal"]["coordinates"]["y"] = y
    data["goal"]["coordinates"]["zoneN"] = cmerc[2]
    data["goal"]["coordinates"]["zoneL"] = cmerc[3]
    
    #Obstacles
    loc = 0
    loc2 = 0
    #print("length of obstacles: {0}\nObstacle1: {1}\n".format(len(data["obstacles"]), data["obstacles"][0]))
    #print(data["obstacles"][loc]["obstacle_info"]["name"])

    if "obstacles" not in data:
        print("No Obstacles")
    else:
            while loc < len(data["obstacles"]):
                while loc2 < len(data["obstacles"][loc]["obstacle_info"]["coordinates"]):
                    cmerc = utm.from_latlon(data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["latitude"], data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["longitude"])
                    x = round(cmerc[0], 1)
                    y = round(cmerc[1], 1)
                    data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["x"] = x
                    data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["y"] = y
                    data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["zoneN"] = cmerc[2]
                    data["obstacles"][loc]["obstacle_info"]["coordinates"][loc2]["zoneL"] = cmerc[3]

                    loc2 += 1
                #Data checking to make sure rectangle has correct num of points
                if (data["obstacles"][loc]["obstacle_info"]["name"] == "rectangle"):
                    if (loc2 != 4):
                        print("WARNING: Obstacle at location {0} of shape rectangle does not have 4 points".format(loc))
                loc += 1
                loc2 = 0
    loc = 0
    loc2 = 0
    # Calculates rectangular boundary width and height

    # Makes polygon into normalized rectangle
    if "obstacles" in data:
        while loc < len(data["obstacles"]):
            #if (data["obstacles"][loc]["obstacle_info"]["name"] == "polygon"):
            #print("\nShape at {0}".format(loc))
            #polynum = len(data["obstacles"][loc]["obstacle_info"]["coordinates"])
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
            #print("\nx_max is {0} | y_max is {1}\nx_min is {2} | y_min is {3}".format(x_max, y_max, x_min, y_min))
            # store max min variables back into intermediate json object
            data["obstacles"][loc]["obstacle_info"]["x_max"] = x_max
            data["obstacles"][loc]["obstacle_info"]["y_max"] = y_max
            data["obstacles"][loc]["obstacle_info"]["x_min"] = x_min
            data["obstacles"][loc]["obstacle_info"]["y_min"] = y_min

            data["obstacles"][loc]["obstacle_info"]["width"] = x_max - x_min
            data["obstacles"][loc]["obstacle_info"]["height"] = y_max - y_min
        
            loc +=1

    #Robot
    cmerc = utm.from_latlon(data["robots"][0]["coordinates"]["latitude"], data["robots"][0]["coordinates"]["longitude"])
    x = round(cmerc[0], 1)
    y = round(cmerc[1], 1)

    data["robots"][0]["coordinates"]["x"] = x
    data["robots"][0]["coordinates"]["y"] = y
    data["robots"][0]["coordinates"]["zoneN"] = cmerc[2]
    data["robots"][0]["coordinates"]["zoneL"] = cmerc[3]
    
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

#new Conversion function
def convert_latlon_to_utm(lat, lon):
    temp = utm.from_latlon(lat, lon)
    Tx = temp[0]
    Ty = temp[1]
    stringx = "{:.0f}".format(Tx)
    stringy = "{:.0f}".format(Ty)

    return Ty




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
