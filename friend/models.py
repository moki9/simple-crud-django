from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Friend(models.Model):
    username = models.CharField('Username', max_length=200, blank=False)
    fname = models.CharField('First Name', max_length=200)
    lname = models.CharField('Last Name', max_length=200)
    email = models.EmailField(blank=False)

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return  reverse('friend_edit', kwargs={'pk': self.pk})       
