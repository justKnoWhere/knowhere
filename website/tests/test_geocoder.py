from django.test import TestCase
from website.utils import GeoCoder


class GeoCoderTest(TestCase):

    ADDRESS = "6220 Culebra Rd, San Antonio, TX 78238"
    COORDINATES = "29.4522704, -98.6101913"

    def test_address_to_coordinates(self):
        calculated_coordinates = GeoCoder.get_coordinates_from_address(self.ADDRESS)
        self.assertEquals(str(calculated_coordinates), self.COORDINATES)

    def test_coordinates_to_address(self):
        calculated_address = GeoCoder.get_address_from_coordinates(self.COORDINATES)
        self.assertEquals(str(calculated_address), self.ADDRESS)
