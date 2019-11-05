#arr = request.data.get('data') #jsonarray에서 학번어레이를 받아옴
import copy
import json

from login.models import UserScheduleDB
from login.serializers import UserScheduleSerializers

arr = [20153159,20175165]
scheduleArr=[]#
data = UserScheduleDB.objects.all()



#temp = temp[0]
dummy = {'student_code': 'blank',
         'time': 'blank',
         'A': 'blank',
         'B': 'blank',
         'C': 'blank',
         'D': 'blank',
         'E': 'blank',
         'F': 'blank'}
for i in range(8):
    scheduleArr.append(dummy) #미리 balnk로 채워두고 쓸꺼임.

for k in arr:
    serializer = UserScheduleSerializers(data.filter(student_code=k), many=True)
    temp = json.dumps(serializer.data, ensure_ascii=False) #한글깨짐방지
    temp = json.loads(temp)


    count = -1
    for i in temp:
        count+=1
        dummy = copy.deepcopy(scheduleArr[count])
        for key, value in i.items():
            if value != 'blank':
                if key != 'time':
                    dummy[key] = 'dummy'
                else:
                    dummy[key] = value
                #print(key,value)
        scheduleArr[count] = dummy
        for key, value in i.items():
            if dummy[key] == 'dummy':
                dummy[key] = 'blank'
            elif dummy[key] == 'blank':
                dummy[key] = 'dummy'
        #print(dummy)
        #print(scheduleArr[count])

print(scheduleArr)
# for i in scheduleArr: #출력확인용
#     print(i)
