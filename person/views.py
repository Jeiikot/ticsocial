from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Person
# Create your views here.
class PersonMain(LoginRequiredMixin, View) :
    def get(self, request):
        count = Person.objects.all().count()
        list_objects = Person.objects.order_by('name')

        ctx = {'person_count': count, 'person_list': list_objects}
        return render(request, 'person/person_list.html', ctx)

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person:index')


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person:index')


class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person:index')