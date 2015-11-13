from django.conf.urls import include, url
from website.views import GroupSearchView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notification_zone/new/$', views.notification_zone_new, name='notification_zone_new'),
    url(r'^notification_zone/(?P<pk>[0-9]+)/$', views.notification_zone_detail, name='notification_zone_detail'),
    url(r'^notification_zones/$', views.notification_zones, name='notification_zones'),
    url(r'^group/new/$', views.group_new, name='group_new'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^group/(?P<pk>[0-9]+)/adduser$', views.group_adduser, name='group_adduser'),
    url(r'^group/(?P<pk>[0-9]+)/removeuser$', views.group_removeuser, name='group_removeuser'),
    url(r'^group/(?P<pk>[0-9]+)/removal$', views.group_removal, name='group_removal'),
    url(r'^groups/$', views.groups_my_list, name='groups_my_list'),
    url(r'^groups/search/?$', GroupSearchView.as_view(), name='group_search'),
    url(r'^notification/new/$', views.notification_new, name='notification_new'),
    url(r'^notification/(?P<pk>[0-9]+)/$', views.notification_detail, name='notification_detail'),
    url(r'^notifications/current/$', views.notifications_current, name='notifications_current'),
    url(r'^notifications/past/$', views.notifications_past, name='notifications_past'),
    url(r'^user/(?P<username>\w+)/$', views.user_profile, name='user_profile')
]