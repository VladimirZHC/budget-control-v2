
from pygments import highlight
from rest_framework import serializers
from .models import Operation


class ControlSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='operation-highlight', format='html')
    class Meta:
        model = Operation
        fields = ('id', 'highlight', 'title', 'transaction', 'pub_date', 'total')

        
        

    