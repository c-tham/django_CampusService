from __future__ import unicode_literals

from django.db import models

# Create your models here.

import re
CAMPUSID_REGEX = re.compile(r'\*[0-9]{8}')
PHONE_REGEX = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
EXTNUM_REGEX = re.compile(r'\d{4}')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATE_REGEX = re.compile(r'19|20[0-9]{2}-[0-9]{2}-[0-9]{2}')

from datetime import datetime, timedelta

class PersonManager(models.Manager):
    def person_validator(self, postData):
        errors = {}
        today = str(datetime.now())[:10] 
        year12 = str(datetime.now()+ timedelta(days=-4380))[:10] # 4380 = 12 years
        print today, year12

        if len(postData['inputCampusID']) < 9 or not CAMPUSID_REGEX.match(postData['inputCampusID']):
            errors["1error01a"] = "The mininum of 9 characters in campus ID: *99999999."

        if len(postData['inputLastName']) < 3:
            errors["1error02"] = "The mininum of 3 characters in first name."

        if len(postData['inputFirstName']) < 3:
            errors["1error03"] = "The mininum of 3 characters in first name."

        if len(postData["inputDateBirth"]) < 10 or not DATE_REGEX.match(postData["inputDateBirth"]):
            errors["1error04a"] = "Invalid date format in date of birth."
        elif str(postData["inputDateBirth"]) > year12:
            errors["1error04b"] = "The person should be at least 12 years old!"

        if len(postData['inputAddress']) < 5:
            errors["1error05"] = "The mininum of 5 characters in address."
        
        if len(postData["inputPhone"]) < 9 or not PHONE_REGEX.match(postData["inputPhone"]):
            errors["1error06"] = "Invalid phone number format: 999-999-9999."

        if len(postData["inputExtNum"]) < 4 or not EXTNUM_REGEX.match(postData["inputExtNum"]):
            errors["1error07"] = "Invalid extension number format: 9999."

        if len(postData['inputEmail']) < 7 or not EMAIL_REGEX.match(postData['inputEmail']):
            errors["1error08"] = "Invalid email address!"

        if len(postData['inputPassword1']) < 8:
            errors["1error09a"] = "Password should be more than 8 characters in length!"
        elif len(postData['inputPassword2']) < 8:
            errors["1error09b"] = "Confirm password should be more than 8 characters in length!"
        if postData['inputPassword1'] != postData['inputPassword2']:
            errors["1error09c"] = "Password and confirm password should be matched!"

        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData['inputEmail']) < 7 or len(postData['inputPassword']) < 8:
            errors["2error1"] = "Invalid credentials!"
        return errors


class Person(models.Model):
    campusID = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    dateBirth = models.DateTimeField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    extNum = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)

    objects = PersonManager()

# class Building(models.Model):
#     personID_from = models.ForeignKey(Person, related_name="personIDFrom")
#     buildingName = models.CharField(max_length=255)
#     officeRoom = models.CharField(max_length=255)
#     createdAt = models.DateTimeField(auto_now_add = True)
#     updatedAt = models.DateTimeField(auto_now = True)

class CatalogType(models.Model):
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)

class Catalog(models.Model):
    person_ID = models.ForeignKey(Person, related_name="personIDFrom")
    catalogType_ID = models.ForeignKey(CatalogType, related_name="catalogTypeFrom")
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)






