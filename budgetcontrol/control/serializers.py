from dataclasses import fields
from rest_framework import serializers
from .models import Operation


class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('id', 'title', 'transaction', 'pub_date')
    