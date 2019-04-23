from django.urls import path
from . import views


app_name = "dashboard"

urlpatterns = [
    path("overview/", views.overview, name="overview"),
    path("org_options/", views.create_organization, name="create_org"),
    path("org_options/<int:pk>/", views.update_organization, name="update_org"),
    path('org_options/user_management/', views.user_management, name="user_management"),
]
