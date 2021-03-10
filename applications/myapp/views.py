from django.shortcuts import render
from .models import Person

def init(request):
  #Select from Persons
  persons = Person.objects.all()
  context = {
    'persons' : persons
  }
  return render(request, 'index.html', context)