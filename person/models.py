from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Enter a Name',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")]
    )

    last_name = models.CharField(
        max_length=150,
        help_text='Enter a Last name',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")]
    )

    id_type = models.CharField(
        max_length=150,
        help_text='Enter a ID Type',
    )

    id_number = models.IntegerField(
        help_text='Enter a ID Number',
        default=0
    )
    birthday = models.DateField(
        auto_now=False, auto_created=False, blank=True, null=True
    )

    user = models.CharField(
        max_length=150,
        help_text='Enter a User',
    )

    state = models.BooleanField(
        default=True,
    )

    password = models.CharField(
        max_length=150,
        help_text='Enter a Password',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name