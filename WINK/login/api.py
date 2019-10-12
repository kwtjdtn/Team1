import random
import string

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from login import views
from login.models import UserScheduleDB
from login.serializers import UserScheduleSerializers


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

@api_view(['POST'])
@csrf_exempt
@permission_classes((AllowAny,))
def logincheck(request):
    print(request.data)

    if request.method == 'POST':
        try:
            id=request.data.get('id')
            pw=request.data.get('pw')

            views.logincheck(id, pw)

            _LENGTH = 500  # N자리

            # 숫자 + 대소문자
            string_pool = string.ascii_letters + string.digits

            # 랜덤한 문자열 생성
            token = ""
            for i in range(_LENGTH):
                token += random.choice(string_pool)  # 랜덤한 문자열 하나 선택
            #print(token)
            save_session(request, id, pw, token)
            #print(request.session.get(token, False))



            print (token)
            return JsonResponse({'TOKEN' : token})
        except:
            print("error")
            return JsonResponse({'LOGIN' : 'FAIL'})

def save_session(request, id, pw, token):
    print(id, pw)
    request.session[token]={'userinfo':[id, pw]}
    print('save session')

@api_view(['GET'])
def get_user_info(request):
    if request.method == 'GET':
        data =request.headers.get('Authorization')
        data = data[7:]
        print(data)
        return Response(request.session.get(data, False))
