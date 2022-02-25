
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Operation
from .serializers import ControlSerializer



@csrf_exempt
def operation_list(request):
    if request.method == 'GET':
        operations = Operation.objects.all()
        serializer = ControlSerializer(operations, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ControlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)





@csrf_exempt
def operation_detail(request, pk):
    try:
        operation = Operation.objects.get(pk=pk)
    except Operation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ControlSerializer(operation)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ControlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        operation.delete()
        return HttpResponse(status=204)