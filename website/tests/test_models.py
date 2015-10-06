from django.test import TestCase
from website.models import User, Notification, Group


class UserTest(TestCase):
    USERNAME = "Test Username"
    FIRST_NAME = "John"
    LAST_NAME = "Tester"
    EMAIL_ADDRESS = "johnbo@tester.com"
    PASSWORD = "password"
    SALT = "salt"

    user = User()

    def test_user_creation(self):
        self.given_a_new_user_is_created()
        self.then_the_user_has_expected_values()

    def given_a_new_user_is_created(self):
        self.user = User.objects.create(
            username=self.USERNAME,
            first_name=self.FIRST_NAME,
            last_name=self.LAST_NAME,
            email_address=self.EMAIL_ADDRESS,
            password=self.PASSWORD,
            salt=self.SALT
        )

    def then_the_user_has_expected_values(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.username, self.USERNAME)
        self.assertEqual(self.user.first_name, self.FIRST_NAME)
        self.assertEqual(self.user.last_name, self.LAST_NAME)
        self.assertEqual(self.user.email_address, self.EMAIL_ADDRESS)
        self.assertEqual(self.user.password, self.PASSWORD)
        self.assertEqual(self.user.salt, self.SALT)


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
