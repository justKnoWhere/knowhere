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


class NotificationZone(models.Model):
    user = models.ForeignKey(User)
    groups = models.ManyToManyField(Group)
    name = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=64)
    radius = models.DecimalField(max_digits=9, decimal_places=2)

