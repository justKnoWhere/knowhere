from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext, loader
from website.forms import NotificationZoneForm, GroupForm, NotificationForm
from website.models import NotificationZone, Group, Notification


def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render(RequestContext(request)))


def notification_zone_new(request):
    if request.method == "POST":
        form = NotificationZoneForm(request.POST)
        if form.is_valid():
            notification_zone = form.save(commit=False)
            notification_zone.user = request.user
            notification_zone.save()
            return redirect('website.views.notification_zone_detail', pk=notification_zone.pk)
    else:
        form = NotificationZoneForm()
    return render(request, 'website/notification_zone_edit.html', {'form': form})


def notification_zone_detail(request, pk):
    notification_zone = get_object_or_404(NotificationZone, pk=pk)
    return render(request, 'website/notification_zone_detail.html', {'notification_zone': notification_zone})


def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            group.users.add(request.user);
            return redirect('website.views.group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'website/group_edit.html', {'form': form})


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'website/group_detail.html', {'group': group})


def notification_new(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.user = request.user;
            notification.save()
            return redirect('website.views.notification_detail', pk=notification.pk)
    else:
        form = NotificationForm()
    return render(request, 'website/notification_edit.html', {'form': form})


def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    return render(request, 'website/notification_detail.html', {'notification': notification})