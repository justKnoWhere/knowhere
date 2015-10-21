__author__ = 'athornton'

import geocoder
# from geocoder import getCoordinates, getAddress, Coordinates, Address

testAddress = "6220 Culebra Rd, San Antonio, TX 78238"
testLat = 29.451999
testLon = -98.610449
testCoord = geocoder.Coordinates(testLat, testLon)

resultCoords = geocoder.getCoordinates(testAddress)

print "Test lookup = " + str(resultCoords.latitude) + ", " + str(resultCoords.longitude)
print "Test reverse lookup = " + geocoder.addressToString(geocoder.getAddress(testCoord))
