from django.forms import ModelForm
from .models import Person

# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

