__author__ = 'athornton'

from geopy import GoogleV3

geolocator = GoogleV3()


class Coordinates:
    def __init__(self, lat=0.0, lon=0.0):
        self.latitude = lat
        self.longitude = lon


class Address:
    def __init__(self, street="", city="", state="", zip=""):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


def getCoordinates(address):
    location = geolocator.geocode(address)
    coordinates = Coordinates(location.latitude, location.longitude)
    return coordinates


def getAddress(coordinates):
    list = []
    list.append(str(coordinates.latitude))
    list.append(", ")
    list.append(str(coordinates.longitude))
    coordString = ''.join(list)

    location = geolocator.reverse(coordString)
    address = str(location[0].address)
    addressComponents = str.split(address, ',')
    street = addressComponents[0]
    city = addressComponents[1]
    state = str.split(addressComponents[2])[0]
    zip = str.split(addressComponents[2])[1]
    # This will likely only work in the US.  Other countries have more components and/or in a different order.
    # Possibly could work with this using regional settings but eh, not for this effort.
    addressObj = Address(street, city, state, zip)
    return addressObj


def addressToString(address):
    addStr = "" + address.street + address.city + ", " + address.state + " " +  address.zip
    return addStr

