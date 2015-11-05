from django.conf import settings
from django.db import models
from website.utils import Address, GeoRangeChecker
from django.core.mail import send_mass_mail


class Group(models.Model):
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=64)
    groups = models.ManyToManyField(Group)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=64)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title

    def get_formatted_address(self):
        return str(Address(self.address, self.city, self.state, self.zipcode))

    def notify(self):
        user_email_addresses_to_notify = []
        print("Got here: %s" % self)
        for group in self.groups.all():
            print("Group to notify: %s" % group)
            for user in group.users.all():
                print("User to notify: %s" % user)
                for notification_zone in NotificationZone.objects.filter(user=user):
                    is_in_range = GeoRangeChecker.is_in_range_mi(
                        notification_zone.radius,
                        notification_zone.latitude,
                        notification_zone.longitude,
                        self.latitude,
                        self.longitude
                    )
                    if is_in_range:
                        user_email_addresses_to_notify.append(user.email)
        messages = []
        print("Emails to notify: %s" % user_email_addresses_to_notify)
        for email_address in user_email_addresses_to_notify:
            message = ('Notification', 'Here is the message', 'notify@knowhere.com', [email_address])
            messages.append(message)
        send_mass_mail(messages, fail_silently=False)


class NotificationZone(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    groups = models.ManyToManyField(Group, blank=True)
    name = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=64)
    radius = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name