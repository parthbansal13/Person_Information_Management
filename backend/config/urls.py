from django.contrib import admin
from django.urls import path, include
from persons import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.add_person_page, name="add_person"),
    path("persons/", views.person_list_page, name="person_list"),
    path("api/", include("persons.urls")),
]
