from django.contrib import admin
from .models import Organization


class MembershipInline(admin.TabularInline):
    model = Organization.ORG_members.through


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['ORG_name', 'ORG_owner', 'ORG_brief']
    inlines = [
        MembershipInline,
    ]
    exclude = ('ORG_members',)

admin.site.register(Organization, OrganizationAdmin)
