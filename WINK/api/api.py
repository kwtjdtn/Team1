import time

import requests
from django.http import JsonResponse
from django.utils.crypto import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        data =request.headers.get('Token')

        print(data)
        try:
            userinfo = request.session.get(data, False)
            userinfo = userinfo['userinfo']

            Login(userinfo[0],userinfo[1])
            data = UserScheduleDB.objects.all()
            serializer = UserScheduleSerializers(data.filter(student_code=userinfo[0]), many=True)
            return JsonResponse({"data":serializer.data},status=status.HTTP_200_OK)
        except:
            return Response('Fail',status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def ktislogin(request):
    if request.method == 'POST':
        try:
            with requests.Session() as s:
                id = request.data.get('id')
                pw = request.data.get('pw')
                URL = 'https://ktis.kookmin.ac.kr/kmu/com.Login.do?'
                data = {'txt_user_id':id, 'txt_passwd':pw}
                response = s.get(URL,data = data)

                URL2 = 'https://ktis.kookmin.ac.kr/kmu/ucb.Ucb0164rAGet01.do'
                custom_headers = {'Set-Cookie':response.headers['Set-Cookie']}
                response2 = s.post(URL2,custom_headers)
                #print(response2.text) #시간표 긁어온거

                _LENGTH = 500  # N자리
                # 숫자 + 대소문자
                string_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                # 랜덤한 문자열 생성
                token = str(time.time())
                for i in range(_LENGTH):
                    token += random.choice(string_pool)  # 랜덤한 문자열 하나 선택

                print(token)
                save_session(request, id, pw, token)
                print(request.session.get(token,False))
                print(token)
                if(response2.text[1]!='H'):
                    return JsonResponse({"login":"fail"},status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({"TOKEN":token},status=status.HTTP_200_OK)
        except:
            return JsonResponse({"login":"fail"},status=status.HTTP_400_BAD_REQUEST)
