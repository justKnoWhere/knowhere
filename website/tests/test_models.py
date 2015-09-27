from django.test import TestCase
from website.models import User, Notification


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


class NotificationTest(TestCase):
    ID = "1234ABCD"
    NAME = "My Notification"
    NOTIFICATION_GROUP = "My Group"
    ADDRESS = "123 Main St."
    CITY = "San Antonio"
    STATE = "TX"
    ZIPCODE = "12345"
    DATE = "Jan 1, 1970"
    TIME = "12:00 AM"

    notification = Notification()

    def test_user_creation(self):
        self.given_a_new_notification_is_created()
        self.then_the_notification_has_expected_values()

    def given_a_new_notification_is_created(self):
        self.notification = Notification.objects.create(
            id=self.ID,
            name=self.NAME,
            address=self.ADDRESS,
            city=self.CITY,
            state=self.STATE,
            zipcode=self.zipcode,
            date=self.DATE,
            time=self.TIME
        )

    def then_the_user_has_expected_values(self):
        self.assertTrue(isinstance(self.notification, Notification))
        self.assertEqual(self.notification.id, self.ID)
        self.assertEqual(self.notification.name, self.NAME)
        self.assertEqual(self.notification.address, self.ADDRESS)
        self.assertEqual(self.notification.city, self.CITY)
        self.assertEqual(self.notification.state, self.STATE)
        self.assertEqual(self.notification.zipcode, self.ZIPCODE)
        self.assertEqual(self.notification.date, self.DATE)
        self.assertEqual(self.notification.time, self.TIME)