from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext, loader
from website.forms import NotificationZoneForm
from website.models import NotificationZone


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
