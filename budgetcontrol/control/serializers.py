from rest_framework import serializers
from .models import Operation, Tag
from django.utils import timezone

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)



class ControlSerializer(serializers.HyperlinkedModelSerializer):
    day = serializers.DateTimeField(source='pub_date', format='%H:%M:%S %d/%m/%Y', default=timezone.now)
    # tags = TagSerializer(many=True)
    class Meta:
        model = Operation
        fields = ('id', 'title', 'transaction', 'day', 'tags')
        
