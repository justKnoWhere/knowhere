from django.test import TestCase
from website.models import Group, Notification, NotificationZone
from django.contrib.auth import get_user_model
from django.core import mail

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

        self.group = Group.objects.create(admin=user1, name=self.NAME)
        self.group.users.add(user1, user2)

    def then_the_group_has_expected_values(self):
        group_users = self.group.users.all()
        self.assertTrue(isinstance(self.group, Group))
        self.assertEqual(self.group.name, self.NAME)
        self.assertEqual(group_users[0].username, self.USERNAME_1)
        self.assertEqual(group_users[1].username, self.USERNAME_2)


class NotificationTest(TestCase):
    USERNAME_1 = "notificationUser1"
    EMAIL_ADDRESS_1 = "notificationUser1@bobmail.info"
    USERNAME_2 = "notificationUser2"
    EMAIL_ADDRESS_2 = "notificationUser2@bobmail.info"

    GROUP_NAME_1 = "My Group 1"
    GROUP_NAME_2 = "My Group 2"

    ZONE_NAME_1 = "My Notification Zone 1"
    ZONE_NAME_2 = "My Notification Zone 2"
    RADIUS = "1.0"

    TITLE = "My Notification"
    ADDRESS = "6220 Culebra Rd"
    CITY = "San Antonio"
    STATE = "TX"
    ZIPCODE = "78238"
    DATE = "1970-01-01"
    TIME = "12:00 AM"
    LATITUDE = 29.4522704
    LONGITUDE = -98.6101913

    notification = Notification()
    group_1 = Group()
    group_2 = Group()
    user_1 = User()
    user_2 = User()

    def test_notification_creation(self):
        self.given_groups_with_users()
        self.when_the_notification_is_created()
        self.then_the_notification_has_expected_values()

    def test_notify(self):
        self.given_groups_with_users()
        self.when_the_notification_is_created()
        self.when_the_notification_is_sent()
        self.then_the_notifications_are_sent()

    def given_users(self):
        self.user_1 = User.objects.create(username=self.USERNAME_1, password="password", email=self.EMAIL_ADDRESS_1)
        self.user_2 = User.objects.create(username=self.USERNAME_2, password="password", email=self.EMAIL_ADDRESS_2)
        NotificationZone.objects.create(
            user=self.user_1,
            name=self.ZONE_NAME_1,
            address=self.ADDRESS,
            city=self.CITY,
            state=self.STATE,
            zipcode=self.ZIPCODE,
            latitude=self.LATITUDE,
            longitude=self.LONGITUDE,
            radius=self.RADIUS
        )
        NotificationZone.objects.create(
            user=self.user_2,
            name=self.ZONE_NAME_2,
            address=self.ADDRESS,
            city=self.CITY,
            state=self.STATE,
            zipcode=self.ZIPCODE,
            latitude=self.LATITUDE,
            longitude=self.LONGITUDE,
            radius=self.RADIUS
        )

    def given_groups_with_users(self):
        self.given_users()
        self.group_1 = Group.objects.create(admin=self.user_1, name=self.GROUP_NAME_1)
        self.group_2 = Group.objects.create(admin=self.user_1, name=self.GROUP_NAME_2)
        self.group_1.users.add(self.user_1, self.user_2)

    def when_the_notification_is_created(self):
        self.notification = Notification.objects.create(
            user=self.user_1,
            title=self.TITLE,
            address=self.ADDRESS,
            city=self.CITY,
            state=self.STATE,
            zipcode=self.ZIPCODE,
            date=self.DATE,
            time=self.TIME,
            latitude=self.LATITUDE,
            longitude=self.LONGITUDE
        )
        self.notification.groups.add(self.group_1, self.group_2)

    def when_the_notification_is_sent(self):
        self.notification.notify()

    def then_the_notification_has_expected_values(self):
        notification_groups = self.notification.groups.all()
        self.assertTrue(isinstance(self.notification, Notification))
        self.assertEqual(self.notification.user.username, self.USERNAME_1)
        self.assertEqual(notification_groups[0].name, self.GROUP_NAME_1)
        self.assertEqual(notification_groups[1].name, self.GROUP_NAME_2)
        self.assertEqual(self.notification.title, self.TITLE)
        self.assertEqual(self.notification.address, self.ADDRESS)
        self.assertEqual(self.notification.city, self.CITY)
        self.assertEqual(self.notification.state, self.STATE)
        self.assertEqual(self.notification.zipcode, self.ZIPCODE)
        self.assertEqual(self.notification.date, self.DATE)
        self.assertEqual(self.notification.time, self.TIME)

    def then_the_notifications_are_sent(self):
        self.assertEqual(len(mail.outbox), 2)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].to[0], self.user_1.email)
        self.assertEqual(mail.outbox[1].to[0], self.user_2.email)


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
        group1 = Group.objects.create(admin=user, name=self.GROUP_NAME_1)
        group2 = Group.objects.create(admin=user, name=self.GROUP_NAME_2)

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
