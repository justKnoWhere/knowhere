from website.models import NotificationZone
from django.forms import ModelForm


class NotificationZoneForm(ModelForm):
    class Meta:
        model = NotificationZone
        exclude = ['user']