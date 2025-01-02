from rest_framework import serializers
from .models import User, Contact, Spam

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'is_spam']

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = ['id', 'phone_number', 'reported_by']