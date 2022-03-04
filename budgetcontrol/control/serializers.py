from rest_framework import serializers
from .models import Operation, Tag
from django.utils import timezone


class ControlSerializer(serializers.HyperlinkedModelSerializer):
    day = serializers.DateTimeField(source='pub_date', format='%H:%M:%S %d/%m/%Y', default=timezone.now)
    class Meta:
        model = Operation
        fields = ('id', 'title', 'transaction', 'day', 'tags')
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'