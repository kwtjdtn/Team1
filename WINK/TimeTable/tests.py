from django.test import TestCase

# Create your tests here.
from TimeTable.models import TimeTable

data = TimeTable.objects.all()
monData = data.filter(student_code='20153159',day='mon')
tueData = data.filter(student_code='20153159',day='tue')

for model_instance in monData:
    print(model_instance.table09_00)
    print(model_instance.table09_30)
    print(model_instance.table10_00)
    print(model_instance.table10_30)
    print(model_instance.table11_00)

for model_instance in tueData:
    print(model_instance.table09_00)
    print(model_instance.table09_30)
    print(model_instance.table10_00)
    print(model_instance.table10_30)
    print(model_instance.table11_00)
