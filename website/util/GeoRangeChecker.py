from math import radians, sin, cos, sqrt, asin

__author__ = 'Adam'

kmInMile = 0.62137119


def isInRange(range, originLat, originLon, destinationLat, destinationLon):
    return haversine(originLat, originLon, destinationLat, destinationLon) <= range


def getDistanceKm(originLat, originLon, destinationLat, destinationLon):
    return haversine(originLat, originLon, destinationLat, destinationLon)


def getDistanceMi(originLat, originLon, destinationLat, destinationLon):
    return haversine(originLat, originLon, destinationLat, destinationLon) * kmInMile


def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c
