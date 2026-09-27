from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("person_name", "mobile_number", "age", "city", "state", "post_code")
    search_fields = ("person_name", "mobile_number", "city", "state")
