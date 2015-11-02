from math import radians, sin, cos, sqrt, asin
from geopy.geocoders import GoogleV3
from geopy.distance import vincenty


class Coordinates(object):
    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    def __str__(self):
        return "%s, %s" % (self.latitude, self.longitude)


class Address(object):
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return "%s, %s, %s %s" % (self.street, self.city, self.state, self.zip)


class GeoRangeChecker(object):

    @classmethod
    def is_in_range_km(cls, range, origin_lat, origin_lon, destination_lat, destination_lon):
        return cls.get_distance_in_km(origin_lat, origin_lon, destination_lat, destination_lon) <= range

    @classmethod
    def is_in_range_mi(cls, range, origin_lat, origin_lon, destination_lat, destination_lon):
        return cls.get_distance_in_mi(origin_lat, origin_lon, destination_lat, destination_lon) <= range

    @classmethod
    def get_distance_in_km(cls, origin_lat, origin_lon, destination_lat, destination_lon):
        distance_in_km = cls.get_distance(origin_lat, origin_lon, destination_lat, destination_lon).kilometers
        return round(distance_in_km, 4)

    @classmethod
    def get_distance_in_mi(cls, origin_lat, origin_lon, destination_lat, destination_lon):
        distance_in_mi = cls.get_distance(origin_lat, origin_lon, destination_lat, destination_lon).miles
        return round(distance_in_mi, 4)

    @classmethod
    def get_distance(cls, origin_lat, origin_lon, destination_lat, destination_lon):
        return vincenty((origin_lat, origin_lon), (destination_lat, destination_lon))


# This will likely only work in the US.  Other countries have more components and/or in a different order.
# Possibly could work with this using regional settings but eh, not for this effort.
class GeoCoder(object):
    geolocator = GoogleV3()

    @classmethod
    def get_coordinates_from_address(cls, address):
        location = cls.geolocator.geocode(address)
        return Coordinates(location.latitude, location.longitude)

    @classmethod
    def get_address_from_coordinates(cls, coordinates):
        location = cls.geolocator.reverse(str(coordinates), True)
        address = location.address
        print(address)
        split_address = str.split(address, ',')
        street = split_address[0].strip()
        city = split_address[1].strip()
        state_and_zip_code = split_address[2].strip().split()
        state = state_and_zip_code[0]
        zip_code = state_and_zip_code[1]

        print(split_address)
        print(street)
        print(city)
        print(state)
        print(zip_code)

        return Address(street, city, state, zip_code)