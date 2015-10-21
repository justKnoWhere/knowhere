from website.models import NotificationZone, Group
from django.forms import ModelForm


class NotificationZoneForm(ModelForm):
    class Meta:
        model = NotificationZone
        exclude = ['user']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ['users']