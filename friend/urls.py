from django.conf.urls import url

from .views import (
    FriendCreate,
    FriendList,
    FriendUpdate,
    FriendDelete,
    )

urlpatterns = [
    url(r'^$', FriendList.as_view(), name='friend_list'),
    url(r'^create/$', FriendCreate.as_view(), name='friend_create'),
    url(r'^(?P<pk>\d+)/edit/$', FriendUpdate.as_view(), name='friend_edit'),
    url(r'^(?P<pk>\d+)/delete/$', FriendDelete.as_view(), name='friend_delete'),
    ]