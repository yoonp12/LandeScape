from __future__ import unicode_literals
from django.db import models
import re


class UserManager(models.Manager):
    def register(self, postData):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{8,}$')

        errors = {}

        if len(postData['email']) < 1:
            errors["email"] = "Email is required"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email-invalid"] = 'Invalid Email!'
        check = User.objects.filter(email=postData['email'].lower())
        if len(check) > 0:
            errors["email-inuse"] = 'Email already in use'

        if len(postData['password']) < 8:
            errors['password'] = 'Password is required!'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 1 number and capitalization!'
        
        if len(postData['password_confirm']) < 1:
            errors['password_confirm'] = 'Confirm password is required!'
        elif postData['password_confirm'] != postData['password']:
            errors['passwords_match'] = 'Password must match Confirm password!'

        return errors

    def login(self, postData):
        errors = {}

        if len(postData['email']) < 1:
            errors['email'] = 'Email is required'

        if len(postData['password']) < 1:
            errors['password'] = 'Password is required'

        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Trail(models.Model):
    trail_id = models.IntegerField()
    name = models.CharField(max_length=255)
    summary = models.TextField()
    difficulty = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    favorite = models.ForeignKey(User, related_name="trails", on_delete=models.CASCADE)

    completed = models.ForeignKey(User, related_name="completed", on_delete=models.CASCADE)


    def __repr__(self):
        return f"<User object: {self.email}>"