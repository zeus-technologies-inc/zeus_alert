from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class Organization(models.Model):
    ORG_name = models.CharField(_("Organization Name"), max_length=100)
    # the owner/ creator of organization
    ORG_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organization_owned')
    ORG_members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users', blank=True)
    # ORG_num_of_users = models.PositiveIntegerField()  ==> get the num from members field instead
    ORG_brief = models.TextField(_("Who are we ?"), max_length=250)
    ORG_created = models.DateTimeField(auto_now_add=True)

    ORG_updated = models.DateTimeField(auto_now=True)
    # ORG_event = models.TextField(_("Event"), max_length=300)  ==> make it separated model if t will be used
    # ORG_position =

    def __str__(self):
        return self.ORG_name

    def get_absolute_url(self):
        return reverse('dashboard:update_org', args=[self.pk])

    def add_user(self):
        """staff user add member/s to the organization"""
        pass

    def del_user(self):
        """staff user delete member/s to the organization"""
        pass

