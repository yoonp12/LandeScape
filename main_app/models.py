from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField
from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def reg_validator(self, postData):

        #RegEx for email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #RegEx for Password
        PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{8,}$')
        errors = {}

    #----Names-----
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long"
    #-----Email-----
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please input a valid email address"
        else:
            for user in User.objects.all():
                if postData['email'] == user.email:
                    errors['email'] = "Email already exists in our system! Please login!"
    #-----Password-----
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif postData['password'] != postData['pass_conf']:
            errors['pass_conf'] == "Passwords do not match!"
        return errors
    
    def log_validator(self, postData):
        errors = {}
        user_info = User.objects.filter(email = postData['email_input'])
        if not user_info:
            errors['email_input'] = "Email does not exist. Please register before logging in!"
        else:
            user = User.objects.get(email=postData['email_input'])
            if not bcrypt.checkpw(postData['password_input'].encode(), user.password.encode()):
                errors['password_input'] = "Password or Email information is not correct!"
        return errors

    def not_logged_validator(self, postData):
        errors = {}
        errors['no'] = "Please log in before entering site."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    hometown = models.CharField(max_length=200)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class favoriteTrail(models.Model):
    trail_id = models.IntegerField()
    user = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)

class completedTrail(models.Model):
    trail_id = models.IntegerField()
    user = models.ForeignKey(User, related_name="completed", on_delete=models.CASCADE)
    


    def __repr__(self):
        return f"<User object: {self.email}>"