from rest_framework import serializers
from .models import HistoryOperation, Operation, Tag
from django.utils import timezone




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ControlSerializer(serializers.ModelSerializer):
    day = serializers.DateTimeField(source='pub_date', format='%H:%M:%S %d/%m/%Y', default=timezone.now)
    update_day = serializers.DateTimeField(source='updated_date', format='%H:%M:%S %d/%m/%Y', default=timezone.now)
    class Meta:
        model = Operation
        fields = ('id', 'title', 'transaction', 'day', 'update_day', 'tags')
        

# class HistorySerializer(ControlSerializer):
#     history_date = serializers.DateTimeField(format='%H:%M:%S %d/%m/%Y')
#     pub_date = serializers.DateTimeField(format='%H:%M:%S %d/%m/%Y')
#     class Meta:
#         model = Operation.history.model
#         fields = ('history_id', 'history_date', 'pub_date', 'title', 'transaction')
        

class HistoryOperationSerializer(serializers.ModelSerializer):
    operation_id = serializers.CharField()
    history_id = serializers.CharField(source='id')
    up_day = serializers.DateTimeField(format='%H:%M:%S %d/%m/%Y')
    class Meta:
        model = HistoryOperation
        fields = ('operation_id', 'history_id', 'title', 'up_day', 'transaction', 'tags')
        
        

