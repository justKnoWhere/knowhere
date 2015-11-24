from django.conf.urls import url
from . import views
from website.views import GroupSearchView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notification_zone/new/$', views.notification_zone_new, name='notification_zone_new'),
    url(r'^notification_zone/(?P<pk>[0-9]+)/$', views.notification_zone_detail, name='notification_zone_detail'),
    url(r'^notification_zones/$', views.notification_zones, name='notification_zones'),
    url(r'^group/new/$', views.group_new, name='group_new'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^group/(?P<pk>[0-9]+)/join$', views.group_join, name='group_join'),
    url(r'^group/(?P<pk>[0-9]+)/request_join$', views.group_request_join, name='group_request_join'),
    url(r'^group/(?P<pk>[0-9]+)/leave$', views.group_leave, name='group_leave'),
    url(r'^group/(?P<pk>[0-9]+)/delete$', views.group_delete, name='group_delete'),
    url(r'^group/(?P<pk>[0-9]+)/add_user/(?P<user_id>[0-9]+)$', views.group_add_user, name='group_search'),
    url(r'^groups/$', views.groups_my_list, name='groups_my_list'),
    url(r'^groups/search/?$', GroupSearchView.as_view(), name='group_search'),
    url(r'^notification/new/$', views.notification_new_or_edit, name='notification_new'),
    url(r'^notification/(?P<pk>[0-9]+)/$', views.notification_detail, name='notification_detail'),
    url(r'^notification/(?P<pk>[0-9]+)/edit$', views.notification_new_or_edit, name='notification_edit'),
    url(r'^notifications/current/$', views.notifications_current, name='notifications_current'),
    url(r'^notifications/past/$', views.notifications_past, name='notifications_past'),
    url(r'^user/(?P<username>\w+)/$', views.user_profile, name='user_profile')
]