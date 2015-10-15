from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from website.forms import NotificationZoneForm


def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render(RequestContext(request)))


def notification_zone_new(request):
    form = NotificationZoneForm()
    return render(request, 'website/notification_zone_edit.html', {'form': form})


def notification_zone_detail(request):
    form = NotificationZoneForm()
    return render(request, 'website/notification_zone_edit.html', {'form': form})
