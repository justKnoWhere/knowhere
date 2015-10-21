from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notification_zone/new/$', views.notification_zone_new, name='notification_zone_new'),
    url(r'^notification_zone/(?P<pk>[0-9]+)/$', views.notification_zone_detail, name='notification_zone_detail'),
    url(r'^group/new/$', views.group_new, name='group_new'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^notification/new/$', views.notification_new, name='notification_new'),
    url(r'^notification/(?P<pk>[0-9]+)/$', views.notification_detail, name='notification_detail'),
]