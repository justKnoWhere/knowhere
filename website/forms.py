from website.models import NotificationZone, Group, Notification
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NotificationZoneForm(ModelForm):
    helper = FormHelper()
    helper.form_tag
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = NotificationZone
        exclude = ['user']


class GroupForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Group
        exclude = ['users']


class NotificationForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Notification
        exclude = ['user']