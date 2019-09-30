from django.test import TestCase

# Create your tests here.
from login.models import UserScheduleDB
from login.serializers import UserScheduleSerializers
def __main__(request):
    request.method={"student_code":"1",	"time":"1",	"A":"1", "B":"1", "C":"1", "D":"1", "E":"1", "F":"1"}
    serializer = UserScheduleSerializers(data=request.data)
    print(serializer.data)