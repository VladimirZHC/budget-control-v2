from .models import Operation
from .serializers import ControlSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from .models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'operations': reverse('operation-list', request=request, format=format)
    })



# class OperationList(generics.ListCreateAPIView):
#     queryset = Operation.objects.all()
#     serializer_class = ControlSerializer
    
# class OperationDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Operation.objects.all()
#     serializer_class = ControlSerializer

# class OperationHighlight(generics.GenericAPIView):
#     queryset = Operation.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]
    
#     def get(self, request, *args, **kwargs):
#         operation = self.get_object()
#         return Response(operation)

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = ControlSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        operation = self.get_object()
        return Response(operation)