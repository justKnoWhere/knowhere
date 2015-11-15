from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template import RequestContext, loader
from website.forms import NotificationZoneForm, GroupForm, GroupRemovalForm, NotificationForm, GroupSearchForm
from website.models import NotificationZone, Group, Notification
from website.utils import GeoCoder, Address
from django.contrib.auth import get_user_model
from django.db.models import Q
from haystack.generic_views import SearchView, SearchQuerySet
import datetime

User = get_user_model()


def group_admin_required(view_function):
    def _wrapped_view_function(request, pk):
        group = get_object_or_404(Group, pk=pk)
        if group.admin == request.user:
            return view_function(group)
        else:
            return HttpResponseForbidden('<h1>Only the group admin can access this command</h1>')
    return _wrapped_view_function


def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render(RequestContext(request)))


def notification_zone_new(request):
    if request.method == "POST":
        form = NotificationZoneForm(request.POST)
        if form.is_valid():
            coordinates = GeoCoder.get_coordinates_from_address(
                Address(form.cleaned_data["address"],
                        form.cleaned_data["city"],
                        form.cleaned_data["state"],
                        form.cleaned_data["zipcode"]
                        )
            )
            notification_zone = form.save(commit=False)
            notification_zone.user = request.user
            notification_zone.latitude = str(coordinates.latitude)
            notification_zone.longitude = str(coordinates.longitude)
            notification_zone.save()
            return redirect('website.views.notification_zone_detail', pk=notification_zone.pk)
    else:
        form = NotificationZoneForm()
    return render(request, 'website/notification_zone_edit.html', {'form': form})


def notification_zone_detail(request, pk):
    notification_zone = get_object_or_404(NotificationZone, pk=pk)
    return render(request, 'website/notification_zone_detail.html', {'notification_zone': notification_zone})


def notification_zones(request):
    user_notification_zones = NotificationZone.objects.filter(user=request.user)
    return render(request, 'website/notification_zones.html', {'notification_zones': user_notification_zones})


def group_adduser(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.users.add(request.user)
    return render(request, 'website/group_detail.html', {'group': group})


def group_removeuser(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.users.remove(request.user)
    return render(request, 'website/group_detail.html', {'group': group})


def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            group.users.add(request.user);
            return redirect('website.views.group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'website/group_edit.html', {'form': form})


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'website/group_detail.html', {'group': group, 'is_admin': is_admin})


@group_admin_required
def group_delete(group):
    group.delete()
    return redirect('groups_my_list')


def groups_my_list(request):
    groups = Group.objects.filter(users=request.user).order_by('-id')
    return render(request, 'website/groups.html', {'groups': groups})


def notification_new(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            coordinates = GeoCoder.get_coordinates_from_address(
                Address(form.cleaned_data["address"],
                        form.cleaned_data["city"],
                        form.cleaned_data["state"],
                        form.cleaned_data["zipcode"]
                        )
            )
            print("Form: %s", form.cleaned_data)
            notification = form.save(commit=False)
            notification.latitude = str(coordinates.latitude)
            notification.longitude = str(coordinates.longitude)
            notification.user = request.user
            notification.save()

            for group in form.cleaned_data['groups']:
                notification.groups.add(group)
            notification.save()

            notification.notify()
            return redirect('website.views.notification_detail', pk=notification.pk)
    else:
        form = NotificationForm()
    return render(request, 'website/notification_edit.html', {'form': form})


def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    return render(request, 'website/notification_detail.html', {'notification': notification})


def notifications_current(request):
    now = datetime.datetime.now()
    notifications = Notification.objects.filter(
                                            user=request.user
                                        ).filter(
                                            Q(date=now.date(),time__gte=now.time())|Q(date__gt=now.date())
                                        ).order_by('-date')
    return render(request, 'website/notifications.html', {'notifications': notifications})


def notifications_past(request):
    now = datetime.datetime.now()
    notifications = Notification.objects.filter(
                                            user=request.user
                                        ).filter(
                                            Q(date=now.date(),time__lte=now.time())|Q(date__lt=now.date())
                                        ).order_by('-date')
    return render(request, 'website/notifications.html', {'notifications': notifications})


def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'website/user_profile.html', {'user': user})


class GroupSearchView(SearchView):
    template_name = "website/group_search.html"
    form_class = GroupSearchForm
