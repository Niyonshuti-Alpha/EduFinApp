from django.http import JsonResponse
from django.shortcuts import render
from core.models import Testing
from core.serializers import TestingSerializer

def testing_view(request):
    testings = Testing.objects.all()
    serializer = TestingSerializer(testings, many=True)
    return JsonResponse(serializer.data, safe=False)

def testing_detail_view(request, id):
    try:
        testing = Testing.objects.get(id=id)
        serializer = TestingSerializer(testing)
        return JsonResponse(serializer.data)
    except Testing.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)