from django.test import TestCase
from website.models import Group, Notification, NotificationZone
from django.contrib.auth import get_user_model

User = get_user_model()


class GroupTest(TestCase):
    NAME = "Test Group"
    USERNAME_1 = "user1"
    USERNAME_2 = "user2"

    group = Group()

    def test_group_creation(self):
        self.given_group_is_created()
        self.then_the_group_has_expected_values()

    def given_group_is_created(self):
        user1 = User.objects.create(username=self.USERNAME_1)
        user2 = User.objects.create(username=self.USERNAME_2)

        self.group = Group.objects.create(name=self.NAME)
        self.group.users.add(user1, user2)

    def then_the_group_has_expected_values(self):
        group_users = self.group.users.all()
        self.assertTrue(isinstance(self.group, Group))
        self.assertEqual(self.group.name, self.NAME)
        self.assertEqual(group_users[0].username, self.USERNAME_1)
        self.assertEqual(group_users[1].username, self.USERNAME_2)


class NotificationTest(TestCase):
    USERNAME = "notificationUser"
    TITLE = "My Notification"
    GROUP_NAME_1 = "My Group 1"
    GROUP_NAME_2 = "My Group 2"
    ADDRESS = "123 Main St."
    CITY = "San Antonio"
    STATE = "TX"
    ZIPCODE = "12345"
    DATE = "1970-01-01"
    TIME = "12:00 AM"

    notification = Notification()

    def test_notification_creation(self):
        self.given_the_notification_is_created()
        self.then_the_notification_has_expected_values()

    def given_the_notification_is_created(self):
        user = User.objects.create(username=self.USERNAME)
        group1 = Group.objects.create(name=self.GROUP_NAME_1)
        group2 = Group.objects.create(name=self.GROUP_NAME_2)

        self.notification = Notification.objects.create(
            user=user,
            title=self.TITLE,
            address=self.ADDRESS,
            city=self.CITY,
            state=self.STATE,
            zipcode=self.ZIPCODE,
            date=self.DATE,
            time=self.TIME
        )
        self.notification.groups.add(group1, group2)

    def then_the_notification_has_expected_values(self):
        notification_groups = self.notification.groups.all()
        self.assertTrue(isinstance(self.notification, Notification))
        self.assertEqual(self.notification.user.username, self.USERNAME)
        self.assertEqual(notification_groups[0].name, self.GROUP_NAME_1)
        self.assertEqual(notification_groups[1].name, self.GROUP_NAME_2)
        self.assertEqual(self.notification.title, self.TITLE)
        self.assertEqual(self.notification.address, self.ADDRESS)
        self.assertEqual(self.notification.city, self.CITY)
        self.assertEqual(self.notification.state, self.STATE)
        self.assertEqual(self.notification.zipcode, self.ZIPCODE)
        self.assertEqual(self.notification.date, self.DATE)
        self.assertEqual(self.notification.time, self.TIME)


class NotificationZoneTest(TestCase):
    USERNAME = "notificationUser"
    NAME = "My Notification Zone"
    GROUP_NAME_1 = "My Group 1"
    GROUP_NAME_2 = "My Group 2"
    ADDRESS = "123 Main St."
    CITY = "San Antonio"
    STATE = "TX"
    ZIPCODE = "12345"
    LATITUDE = 40.814796
    LONGITUDE = -77.865313
    RADIUS = 1.5

    notification_zone = NotificationZone()

    def test_notification_creation(self):
        self.given_the_notification_is_created()
        self.then_the_notification_has_expected_values()

    def given_the_notification_is_created(self):
        user = User.objects.create(username=self.USERNAME)
        group1 = Group.objects.create(name=self.GROUP_NAME_1)
        group2 = Group.objects.create(name=self.GROUP_NAME_2)

        self.notification_zone = NotificationZone.objects.create(
            user=user,
            name=self.NAME,
            address=self.ADDRESS,
            city=self.CITY,
            state=self.STATE,
            zipcode=self.ZIPCODE,
            latitude=self.LATITUDE,
            longitude=self.LONGITUDE,
            radius=self.RADIUS
        )
        self.notification_zone.groups.add(group1, group2)

    def then_the_notification_has_expected_values(self):
        notification_zone_groups = self.notification_zone.groups.all()
        self.assertTrue(isinstance(self.notification_zone, NotificationZone))
        self.assertEqual(self.notification_zone.user.username, self.USERNAME)
        self.assertEqual(notification_zone_groups[0].name, self.GROUP_NAME_1)
        self.assertEqual(notification_zone_groups[1].name, self.GROUP_NAME_2)
        self.assertEqual(self.notification_zone.name, self.NAME)
        self.assertEqual(self.notification_zone.address, self.ADDRESS)
        self.assertEqual(self.notification_zone.city, self.CITY)
        self.assertEqual(self.notification_zone.state, self.STATE)
        self.assertEqual(self.notification_zone.zipcode, self.ZIPCODE)
        self.assertEqual(self.notification_zone.latitude, self.LATITUDE)
        self.assertEqual(self.notification_zone.longitude, self.LONGITUDE)
        self.assertEqual(self.notification_zone.radius, self.RADIUS)
