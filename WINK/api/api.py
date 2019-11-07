import copy
import time
import json

import requests
from django.http import JsonResponse
from django.utils.crypto import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from login.models import UserScheduleDB
from login.serializers import UserScheduleSerializers
from login.views import Login
from api.insertschedule import scheduleDB
from userinfo.models import NormalUser

from datetime import datetime, timedelta


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


def save_session(request, id, pw, token, expire=None):
    # print(id, pw)
    request.session[token]={'userinfo':[id, pw]}
    request.session.save()
    userinfo = NormalUser.objects.all()
    if (userinfo.filter(id=id, pw=pw)):
        print(expire)
        userinfo.filter(id=id, pw=pw).update(token=token, expire=expire)
        # userinfo.token = token
        # userinfo.expire = expire
        print('login check - already has data')
    else:
        userinfo = NormalUser(id=id, pw=pw, token=token, expire=expire)
        userinfo.save()
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
        data = request.META.get('HTTP_TOKEN')
	
        print(data)
        try:
            userinfo = NormalUser.objects.filter(token=data)
            print(userinfo[0])

            data = UserScheduleDB.objects.all()
            serializer = UserScheduleSerializers(data.filter(student_code=userinfo[0]), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response('Fail', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def ktislogin(request):
    if request.method == 'POST':
        try:
            with requests.Session() as s:
                id = request.data.get('id')
                pw = request.data.get('pw')
                URL = 'https://ktis.kookmin.ac.kr/kmu/com.Login.do?'

                data = {'txt_user_id': id, 'txt_passwd': pw}

                response = s.post(URL,data)

                URL2 = 'https://ktis.kookmin.ac.kr/kmu/ucb.Ucb0164rAGet01.do'
                custom_headers = {'Set-Cookie':response.headers['Set-Cookie']}
                response2 = s.post(URL2, custom_headers)
                #print(response2.text) #시간표 긁어온거
                if (response2.text[1] != 'H'):
                    return JsonResponse({"login": "fail"}, status=status.HTTP_400_BAD_REQUEST)

                _LENGTH = 500  # N자리
                # 숫자 + 대소문자
                string_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                # 랜덤한 문자열 생성
                token = str(time.time())
                token = token[11:]
                for i in range(_LENGTH):
                    token += random.choice(string_pool)  # 랜덤한 문자열 하나 선택
                expire = datetime.now()
                save_session(request, id, pw, token, expire) #세션에 유저정보를 저장함. key = token value = info
                #print(request.session.session_key)
                scheduleDB(id, response2.text) #시간표 DB입력
                res = JsonResponse({"TOKEN": token}, status=status.HTTP_200_OK)
                res.set_cookie('exp', expire)
            return res
        except:
            return JsonResponse({"login": "fail"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def multiply(request):
    try:
        # print(request.data.get('student_code'))
        arr = request.data.get('student_code')
        arr = arr.split(',')
        # print(arr[0], arr[1])
        # arr = [20153159, 20175165]
        scheduleArr = [] #데이터 담아둘 공간
        data = UserScheduleDB.objects.all()

        # temp = temp[0]
        dummy = {'student_code': 'blank',
                 'time': 'blank',
                 'A': 'blank',
                 'B': 'blank',
                 'C': 'blank',
                 'D': 'blank',
                 'E': 'blank',
                 'F': 'blank'}
        for i in range(8):
            scheduleArr.append(dummy)  # 미리 balnk로 채워두고 쓸꺼임.

        for k in arr:
            serializer = UserScheduleSerializers(data.filter(student_code=k), many=True)
            temp = json.dumps(serializer.data, ensure_ascii=False)  # 한글깨짐방지
            temp = json.loads(temp)

            count = -1
            for i in temp:
                count += 1
                dummy = copy.deepcopy(scheduleArr[count])
                for key, value in i.items():
                    if value != 'blank':
                        if key != 'time':
                            dummy[key] = 'dummy'
                        else:
                            dummy[key] = value
                        # print(key,value)

                scheduleArr[count] = dummy
        for i in scheduleArr:
            for key, value in i.items():
                if value == 'dummy':
                    i[key] = 'blank'
                elif value == 'blank':
                    i[key] = '공강'

        # print(scheduleArr)
        # for i in scheduleArr:  # 출력확인용
        #     print(i)
        return JsonResponse({'data': scheduleArr}, status=status.HTTP_200_OK)
    except:
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)
