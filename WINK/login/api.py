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
from login.views import Login


@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':

        print("headers")
        print(request.headers)
        print("body")
        print(request.data)
        return Response(status=status.HTTP_200_OK)

    elif request.method == 'POST':
        print("headers")
        print(request.headers)
        print("body")
        print(request.data)
        return Response(status=status.HTTP_200_OK)

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
        # test=request.session.get(data, False)
        # test=test['userinfo']
        # print(test[0])
        # print(test[1])
        return Response(request.session.get(data, False))

@api_view(['GET'])
def createschedule(request):
    if request.method == 'GET':
        data =request.headers.get('Authorization')
        data = data[7:]
        print(data)
        try:
            userinfo = request.session.get(data, False)
            userinfo = userinfo['userinfo']

            Login(userinfo[0],userinfo[1])
            data = UserScheduleDB.objects.all()
            serializer = UserScheduleSerializers(data.filter(student_code=userinfo[0]), many=True)
            return JsonResponse({"data":serializer.data},status=status.HTTP_200_OK)
        except:
            return Response(False,status=status.HTTP_400_BAD_REQUEST)
