import math


def isCollision(x1, y1, x2, y2, object_size):
    distance = getDistance(x1+30, y1, x2, y2)
    if distance < 30:
        return True
    else:
        return False


def getDistance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + (math.pow(y1 - y2, 2)))