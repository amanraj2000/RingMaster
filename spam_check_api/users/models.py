from django.core.exceptions import ValidationError
from django.db import models
import re

def validate_phone_number(value):
    if not re.match(r'^\d{10}$', value): 
        raise ValidationError('Invalid Phone Number. Phone number must be exactly 10 digits.')

class User(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True, validators=[validate_phone_number], db_index=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number], db_index=True)
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'

class Spam(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, validators=[validate_phone_number], db_index=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number
