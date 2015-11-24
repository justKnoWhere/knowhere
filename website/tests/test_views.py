from django.test import TestCase
from website.models import Group, Notification, NotificationZone
from django.contrib.auth import get_user_model

User = get_user_model()


class NotificationZoneViewTest(TestCase):
    USERNAME = "test_user"
    LATITUDE = "29.452270"
    LONGITUDE = "-98.610191"
    group = Group()

    def test_calculation_of_latitude_and_longitude_on_creation(self):
        self.given_a_logged_in_user_and_group()
        self.when_viewing_the_notification_zone_create_form()
        self.when_creating_a_notification_zone()
        self.then_latitude_and_longitude_are_calculated_and_saved()

    def given_a_logged_in_user_and_group(self):
        user = User.objects.create(username=self.USERNAME, is_active=True)
        user.set_password("password")
        user.save()
        self.client.login(username=self.USERNAME, password="password")

        self.group = Group.objects.create(admin=user, name="TEST_GROUP")
        self.group.users.add(user)

    def when_viewing_the_notification_zone_create_form(self):
        self.client.get("/notification_zone/new")

    def when_creating_a_notification_zone(self):
        self.response = self.client.post("/notification_zone/new/", {
            "groups" : [self.group.id],
            "name" : "test_notification_zone",
            "address" : "6220 Culebra Rd",
            "city" : "San Antonio",
            "state" : "TX",
            "zipcode" : "78238",
            "radius" : 1.0,
        }, follow=True)

    def then_latitude_and_longitude_are_calculated_and_saved(self):
        notification_zone = self.response.context["notification_zone"]
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(str(notification_zone.latitude), self.LATITUDE)
        self.assertEqual(str(notification_zone.longitude), self.LONGITUDE)