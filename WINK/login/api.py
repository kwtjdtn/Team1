from django.http import JsonResponse

from login.models import UserScheduleDB
from login.serializers import UserScheduleSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class Creater(CreateAPIView):
    def post(self,request,format=None):
        serializer = UserScheduleSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create(request, format=None):
    if request.method == 'GET':
        data = UserScheduleDB.objects.all()
        key = '20153159'
        #key= data.filter(student_code='20153159')[0]
        #print(str(key)[0:8])
        serializer = UserScheduleSerializers(data.filter(student_code = key),many=True)


        result={}
        result[0]=serializer.data
        print(result)

        return JsonResponse({'data':serializer.data})
    elif request.method == 'POST':
        serializer = UserScheduleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
