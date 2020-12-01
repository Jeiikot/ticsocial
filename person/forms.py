from django.forms import ModelForm
from .models import Person

# Create the form class.
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'id_type',
            'id_number',
            'birthday',
            'username',
            'password',
            'is_active',
        )

