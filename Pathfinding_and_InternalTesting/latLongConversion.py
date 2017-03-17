import json
import math

def readJSON(data, scale):

    #globally store JSON message
    Json = json.loads('{}')

    #Boundary
    x = convert_latlong_to_xy(data["boundary"]["boundary_info"][0]["latitude"], scale)
    y = convert_latlong_to_xy(data["boundary"]["boundary_info"][0]["longitude"], scale)
    data["boundary"]["boundary_info"][0]["x"] = x
    data["boundary"]["boundary_info"][0]["y"] = y

    #Goal
    x = convert_latlong_to_xy(data["goal"]["coordinates"]["latitude"], scale)
    y = convert_latlong_to_xy(data["goal"]["coordinates"]["longitude"], scale)
    data["goal"]["coordinates"]["x"] = x
    data["goal"]["coordinates"]["y"] = y

    #Obstacles
    loc = 0
    if "obstacles" not in data:
        print("No Obstacles")
    else:
            while loc < len(data["obstacles"]):
                data["obstacles"][loc]["obstacle_info"][0]["x"] = convert_latlong_to_xy(data["obstacles"][loc]["obstacle_info"][0]["latitude"], scale)
                data["obstacles"][loc]["obstacle_info"][0]["y"] = convert_latlong_to_xy(data["obstacles"][loc]["obstacle_info"][0]["longitude"], scale)
                loc += 1

    #Robot
    x = convert_latlong_to_xy(data["robots"][0]["coordinates"]["latitude"], scale)
    y = convert_latlong_to_xy(data["robots"][0]["coordinates"]["longitude"], scale)

    data["robots"][0]["coordinates"]["x"] = x
    data["robots"][0]["coordinates"]["y"] = y
    
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
    
    return data

'''
This table describes how many decimal places are required for each difference in
position.
decimal
places   degrees          distance
-------  -------          --------
0        1                111  km
1        0.1              11.1 km
2        0.01             1.11 km
3        0.001            111  m
4        0.0001           11.1 m
5        0.00001          1.11 m
6        0.000001         11.1 cm
7        0.0000001        1.11 cm
8        0.00000001       1.11 mm
'''

#Should probably use a scale of 7 giving us a measurable distance of about 1 cm

'''
Program written to convert Latitude and Longitude values to X,Yintergers to be used
for the pathfinding algorithm.
'''

def convert_latlong_to_xy(latOrLongitude, scale):
    
    xyReturn = int(latOrLongitude*(10**scale))

    return xyReturn

# Converts XY coordinates given to it to global Latitude and Longitude Values
def convert_xy_to_latlong(XorY, scale):

    latlongReturn = float(XorY/(10**scale))

    return latlongReturn

"""

def convert_latlong_to_xy(latOrLongitude, scale):
    
    xyReturn = int((latOrLongitude + 180)*(10**scale))
    #xyReturn = latOrLongitude

    return xyReturn

# Converts XY coordinates given to it to global Latitude and Longitude Values
def convert_xy_to_latlong(XorY, scale):

    latlongReturn = float((XorY)/(10**scale))

    retval = latlongReturn - 180

    retval = math.ceil(retval * 1000000) / 1000000

    return retval

"""