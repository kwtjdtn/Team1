from django.db import models

# Create your models here.
from django.db.models import CharField


class TimeTable(models.Model):
    nine = CharField(max_length=50)