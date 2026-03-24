from rest_framework import serializers
from .models import ContactQuery

class ContactQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactQuery
        fields = '__all__'
