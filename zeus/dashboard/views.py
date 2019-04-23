from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CreateOrUpdateOrganization
from.models import Organization


def overview(request):
    all_orgs = Organization.objects.all()
    context = {'all_orgs': all_orgs}
    return render(request, 'dashboard/overview.html', context)


def org_detail(request, pk):
    org = Organization.objects.get(pk=pk)
    context = {'org': org}
    return render(request, 'dashboard/org_detail.html', context)


@staff_member_required
def create_organization(request):
    if request.method == 'POST':
        create_form = CreateOrUpdateOrganization(data=request.POST)
        if create_form.is_valid():
            cd = create_form.cleaned_data
            new_org = Organization.objects.create(ORG_name=cd['ORG_name'], ORG_owner=request.user, ORG_brief=cd['ORG_brief'])
            new_org.save()
    else:
        create_form = CreateOrUpdateOrganization()

    context = {'create_form': create_form}
    return render(request, 'dashboard/create_organization.html', context)


def update_organization(request, pk):
    if request.method == 'POST':
        org_instance = Organization.objects.get(pk=pk)
        update_form = CreateOrUpdateOrganization(data=request.POST, instance=org_instance)
        if update_form.is_valid():
            update_form.save()
    else:
        org_instance = Organization.objects.get(pk=pk)
        update_form = CreateOrUpdateOrganization(instance=org_instance)

    context = {'update_form': update_form, 'org': org_instance}
    return render(request, 'dashboard/org_detail.html', context)


def user_management(request, pk=None):
    all_orgs = request.user.organization_owned.all()
    context = {'all_orgs': all_orgs}
    return render(request, 'dashboard/user_management.html', context)
