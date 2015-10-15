from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notification_zone/new/$', views.notification_zone_new, name='notification_zone_new'),
    url(r'^notification_zone/(?P<pk>[0-9]+)/$', views.notification_zone_detail, name='notification_zone_detail'),
]