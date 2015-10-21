from website.models import NotificationZone, Group, Notification
from django.forms import ModelForm


class NotificationZoneForm(ModelForm):
    class Meta:
        model = NotificationZone
        exclude = ['user']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ['users']


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        exclude = ['user']