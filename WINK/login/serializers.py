from rest_framework import serializers
from .models import UserScheduleDB


class UserScheduleSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserScheduleDB
        fields = ('student_code', 'time', 'A', 'B', 'C', 'D', 'E', 'F')

    def create(self, data):
        return UserScheduleDB.objects.create(**data)