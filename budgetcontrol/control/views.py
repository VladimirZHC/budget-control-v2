from .models import Currency, HistoryOperation, Operation, Tag
from .serializers import ControlSerializer, HistoryOperationSerializer, TagSerializer, CurrencySerializer
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
from rest_framework.views import APIView
import requests




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
        rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        curr = rate['Valute']['USD']['Value']
        total = Decimal(Operation.objects.aggregate(total=Coalesce(Sum('transaction'), Decimal(0.00)))['total'])
        result = super().list(self, request, *args, **kwargs)
        total_in_USD = total / Decimal(curr)
        result.data.update({
            'total_in_RUB': total,
            'currency_of_USD': curr,
            'total_in_USD': total_in_USD
        })
        return Response(result.data)

    

    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    



class HistoryOperationViewSet(viewsets.ModelViewSet):
    serializer_class = HistoryOperationSerializer
    
    def get_queryset(self):
        operation = self.kwargs.get('pk', None)
        queryset = HistoryOperation.objects.filter(operation=operation)
        if queryset:
            return queryset
        raise NotFound()


class CurrencyOperationViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    
    def list(self, request, *args, **kwargs):
        rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        result = super().list(self, request, *args, **kwargs)
        result.data.update({
            'currency': rate,  
        })
        return Response(result.data)

