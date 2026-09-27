from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

def add_person_page(request):
    return render(request, "add_person.html")

def person_list_page(request):
    return render(request, "person_list.html")

class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
