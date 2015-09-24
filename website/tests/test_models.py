from django.test import TestCase
from website.models import User


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