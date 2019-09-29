from django.test import TestCase

# Create your tests here.
from login.models import UserScheduleDB

model_instance = UserScheduleDB.objects.all()
model_instance = model_instance.filter(student_code='20153159')

queryset=len(str(model_instance))
if queryset=='<QuerySet []>':
    print('True')
else:
    print('False')
print(queryset)