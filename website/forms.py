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
        exclude = ['user', 'latitude', 'longitude']


class GroupForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Group
        exclude = ['admin', 'users']


class GroupRemovalForm(ModelForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = 'group_removal'
    helper.add_input(Submit('submit', 'Remove'))

    class Meta:
        model = Group
        exclude = ['users']


class NotificationForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Notification
        exclude = ['user', 'latitude', 'longitude']