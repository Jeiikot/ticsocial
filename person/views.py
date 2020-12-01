from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PersonForm
from .models import Person

# Create your views here.
class PersonMain(LoginRequiredMixin, View) :
    def get(self, request):
        list_objects = Person.objects.filter(is_active=True).order_by('first_name')
        count = list_objects.count()

        ctx = {'person_count': count, 'person_list': list_objects}
        return render(request, 'person/person_list.html', ctx)

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person:index')


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person:index')


class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person:index')