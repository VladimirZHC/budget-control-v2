from rest_framework import serializers
from .models import HistoryOperation, Operation, Tag
from django.utils import timezone
import json




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
        
    
    def create(self, validated_data):
        result = super().create(validated_data)
        
        HistoryOperation.objects.create(
            operation = result,
            title = result.title,
            transaction = result.transaction,
            tags = json.dumps(list(result.tags.values_list(flat=True)))
        )
        return result
    
    def update(self, instance, validated_data):
        res = super().update(instance, validated_data)        

        HistoryOperation.objects.create(
            operation = instance,
            title = instance.title,
            transaction=instance.transaction,
            tags = json.dumps(list(instance.tags.values_list(flat=True)))
        )
        
        return res






class HistoryOperationSerializer(ControlSerializer):
    operation_id = serializers.CharField()
    history_id = serializers.CharField(source='id')
    up_day = serializers.DateTimeField(format='%H:%M:%S %d/%m/%Y')
    
    tags = serializers.SerializerMethodField()
    
    def get_tags(self, obj):
        return json.loads(obj.tags)
    
    
    class Meta:
        model = HistoryOperation
        fields = ('operation_id', 'history_id', 'title', 'up_day', 'transaction', 'tags')
        
        

