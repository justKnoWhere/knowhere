from math import radians, sin, cos, sqrt, asin


class GeoRangeChecker(object):
    km_in_mile = 0.62137119

    @classmethod
    def is_in_range(cls, range_in_km, origin_lat, origin_lon, destination_lat, destination_lon):
        return cls.haversine(origin_lat, origin_lon, destination_lat, destination_lon) <= range_in_km

    @classmethod
    def get_distance_in_km(cls, origin_lat, origin_lon, destination_lat, destination_lon):
        distance_in_km = cls.haversine(origin_lat, origin_lon, destination_lat, destination_lon)
        return round(distance_in_km, 4)

    @classmethod
    def get_distance_in_mi(cls, origin_lat, origin_lon, destination_lat, destination_lon):
        distance_in_mi = cls.haversine(origin_lat, origin_lon, destination_lat, destination_lon) * cls.km_in_mile
        return round(distance_in_mi, 4)

    @classmethod
    def haversine(cls, latitude_1, longitude_1, latitude_2, longitude_2):
        radius_of_earth_in_km = 6372.8

        difference_between_latitudes = radians(latitude_2 - latitude_1)
        difference_between_longitudes = radians(longitude_2 - longitude_1)
        latitude_1 = radians(latitude_1)
        latitude_2 = radians(latitude_2)

        a = sin(difference_between_latitudes / 2) \
            ** 2 + cos(latitude_1) * cos(latitude_2) * sin(difference_between_longitudes / 2) ** 2
        c = 2 * asin(sqrt(a))

        return radius_of_earth_in_km * c
