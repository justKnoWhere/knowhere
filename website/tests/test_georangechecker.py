from GeoRangeChecker import getDistanceKm, getDistanceMi, isInRange

__author__ = 'Adam'

originLat1 = 29.443612
originLon1 = -98.613699

destinationLat1 = 29.452095
destinationLon1 = -98.609837

theRange = 1.015

print "Distance in km: ", getDistanceKm(originLat1, originLon1, destinationLat1, destinationLon1)

print "Distance in mi: ", getDistanceMi(originLat1, originLon1, destinationLat1, destinationLon1)

print "Is within range of ", theRange, "km: ", isInRange(theRange, originLat1, originLon1, destinationLat1,
                                                         destinationLon1)

theRange = 1.0148

print "Is within range of ", theRange, "km: ", isInRange(theRange, originLat1, originLon1, destinationLat1,
                                                         destinationLon1)
