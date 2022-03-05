from .models import Operation, Tag
from .serializers import ControlSerializer, TagSerializer, HistorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from decimal import Decimal
from django.db.models.functions import Coalesce
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import NotFound

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'operations': reverse('operation-list', request=request, format=format)
    })



class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = ControlSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['title', 'pub_date', 'transaction', 'tags']
    search_fields = ['title', ]
    
    def list(self, request, *args, **kwargs):
        result = super().list(self, request, *args, **kwargs)
        result.data.update({
            'total': Decimal(
            Operation.objects
            .aggregate(total=Coalesce(Sum('transaction'), Decimal(0.00)))['total']
        )
        })
        return Response(result.data)
    

    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    

class OperationHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    
    def get_queryset(self):
        id = self.kwargs.get('pk', None)
        queryset = Operation.history.filter(id=id)
        if queryset:
            return queryset
        raise NotFound()
    