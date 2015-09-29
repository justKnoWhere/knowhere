from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.CharField(max_length=254)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=64)


class Notification(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    notification_group = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=64)
    date = models.DateField(max_length=64)
    time = models.DateTimeField(max_length=64)


class Group(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    email = models.CharField(max_lengh=64)
    emailList = models.CharField(max_length=2048)
    #Maybe convert the database entry into JSON string; I'm not really sure how to back a select/combo box