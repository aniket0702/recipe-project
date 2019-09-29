from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Creating a new email is succesfull"""
        email = 'test@gmail.com'
        password = "somethingcool"
        user = get_user_model().objects.create_user(
            email = email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_normalized(self):
        """Creating a new email is normalized"""
        email = 'test@GMAIL.com'
        password = "somethingcool"
        user = get_user_model().objects.create_user(
            email = email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''check if the email is provided'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1223')

    def test_create_new_superuser(self):
        '''Testing to create a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@123.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff) 
