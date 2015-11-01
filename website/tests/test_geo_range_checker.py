from django.test import TestCase

from website.util.geo_range_checker import GeoRangeChecker


class GeoRangeCheckerTest(TestCase):

    ORIGIN_LAT = 29.443612
    ORIGIN_LON = -98.613699

    DESTINATION_LAT = 29.452095
    DESTINATION_LON = -98.609837

    DISTANCE_BETWEEN_POINTS_IN_KM = 1.0150
    DISTANCE_BETWEEN_POINTS_IN_MI = 0.6307

    RANGE_IN_KM = 1.0151

    def test_calculation_of_distance_in_km(self):
        calculated_distance_between_points_in_km = GeoRangeChecker.get_distance_in_km(
            self.ORIGIN_LAT, self.ORIGIN_LON, self.DESTINATION_LAT, self.DESTINATION_LON)
        self.assertEquals(calculated_distance_between_points_in_km, self.DISTANCE_BETWEEN_POINTS_IN_KM)

    def test_calculation_of_distance_in_mi(self):
        calculated_distance_between_points_in_mi = GeoRangeChecker.get_distance_in_mi(
            self.ORIGIN_LAT, self.ORIGIN_LON, self.DESTINATION_LAT, self.DESTINATION_LON)
        self.assertEquals(calculated_distance_between_points_in_mi, self.DISTANCE_BETWEEN_POINTS_IN_MI)

    def test_is_in_range(self):
        destination_points_are_within_range = GeoRangeChecker.is_in_range(
            self.RANGE_IN_KM, self.ORIGIN_LAT, self.ORIGIN_LON, self.DESTINATION_LAT, self.DESTINATION_LON)
        self.assertTrue(destination_points_are_within_range)