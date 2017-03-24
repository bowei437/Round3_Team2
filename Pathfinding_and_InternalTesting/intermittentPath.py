import json
import math
import numpy
from pprint import pprint
from latLongConversion import *
import matplotlib.path as mplPath

### Intermitten Pathfinding ###

## Used to determine where the new partial path will start
def intersectLocation(oldPathX, oldPathY,  newObstacleX, newObstacleY):

    newStartLocation = [-99999, -99999]

    obstaclePathRep = mplPath.Path(numpy.array([[newObstacleX[0], newObstacleY[0]],
                     [newObstacleX[1], newObstacleY[1]],
                     [newObstacleX[2], newObstacleY[2]],
                     [newObstacleX[3], newObstacleY[3]],
                     [newObstacleX[0], newObstacleY[0]]]))

    for i in range(len(oldPathX)):
        if obstaclePathRep.contains_point((oldPathX[i], oldPathY[i])):
            print( "The Path Intersects the new Obstacle")
            newStartLocation[0] = oldPathX[i]
            newStartLocation[1] = oldPathY[i]
            return newStartLocation
        else:
            print("The Path Does Not Intersect the New Obstacle")
            
    return newStartLocation

## Used to determine if a new partial path is needed
def doesPathIntersects(oldPathX, oldPathY,  newObstacleX, newObstacleY):

    obstaclePathRep = mplPath.Path(numpy.array([[newObstacleX[0], newObstacleY[0]],
                     [newObstacleX[1], newObstacleY[1]],
                     [newObstacleX[2], newObstacleY[2]],
                     [newObstacleX[3], newObstacleY[3]],
                     [newObstacleX[0], newObstacleY[0]]]))

    for i in range(len(oldPathX)):
        if obstaclePathRep.contains_point((oldPathX[i], oldPathY[i])):
            print( "The Path Intersects the new Obstacle")
            return True
        else:
            print("The Path Does Not Intersect the New Obstacle")
            
    return False




'''
testObX = [0,0,1,1]
testObY = [0,1,1,0]
testPathX = [0.5,2]
testPathY = [0.5,2]


doesPathIntersects(testPathX, testPathY, testObX, testObY)
'''
