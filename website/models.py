from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.CharField(max_length=254)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=64)


class Group(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=64)


class Notification(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=64)
    groups = models.ManyToManyField(Group)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=64)
    date = models.DateField()
    time = models.TimeField()


