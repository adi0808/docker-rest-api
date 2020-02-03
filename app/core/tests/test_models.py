from django.contrib.auth import get_user_model

# by using get_user_model if anything changes in the User model we just need to update
# the settings file instead of changing the import in every file where it is used

from django.test import TestCase

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "aditya@gmail.com"
        password = "Test123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
            # password check is done this way

    def test_new_user_email_normalized(self):
        """Test the email for the new user is normalized"""
        email = "aditya@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test@1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'aditya@gmail.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
