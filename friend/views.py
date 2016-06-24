from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
    )

from .models import Friend

class FriendList(ListView):
    model = Friend

class FriendCreate(CreateView):
    model = Friend
    success_url = reverse_lazy('friend_list')
    fields = [ 'username', 'fname', 'lname', 'email']

class FriendUpdate(UpdateView):
    model = Friend
    success_url = reverse_lazy('friend_list')
    fields = [ 'username', 'fname', 'lname', 'email']

class FriendDelete(DeleteView):
    model = Friend
    success_url = reverse_lazy('friend_list')
