from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Operation
from .serializers import ControlSerializer



@api_view(['GET', 'POST'])
def operation_list(request, format=None):
    if request.method == 'GET':
        operations = Operation.objects.all()
        serializer = ControlSerializer(operations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ControlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'PUT', 'DELETE'])
def operation_detail(request, pk, format=None):
    try:
        operation = Operation.objects.get(pk=pk)
    except Operation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ControlSerializer(operation)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ControlSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)