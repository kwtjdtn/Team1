from django.http import JsonResponse

from login.models import UserScheduleDB
from login.serializers import UserScheduleSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def create(request):
    if request.method == 'GET':

        print(request.headers.get('Authorization'))
        if(request.headers.get('Authorization')=='Basic d2luazp3aW5r'):
            data = UserScheduleDB.objects.all()
            key = request.query_params.get('student_code')
            serializer = UserScheduleSerializers(data.filter(student_code=key), many=True)
            return JsonResponse({'data' : serializer.data})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'POST':
        #print(request.data)

        serializer = UserScheduleSerializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return JsonResponse(request.data)
