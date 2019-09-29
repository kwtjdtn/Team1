from django.db import models

# Create your models here.

class Schedule(models.Model):
    student_code = models.CharField(max_length=8)
    day = models.CharField(max_length=3,null=True,blank=True)
    table09_00 = models.CharField(max_length=50,null=True,blank=True)
    table09_30 = models.CharField(max_length=50,null=True,blank=True)
    table10_00 = models.CharField(max_length=50,null=True,blank=True)
    table10_30 = models.CharField(max_length=50,null=True,blank=True)
    table11_00 = models.CharField(max_length=50,null=True,blank=True)
    table11_30 = models.CharField(max_length=50,null=True,blank=True)
    table12_00 = models.CharField(max_length=50,null=True,blank=True)
    table12_30 = models.CharField(max_length=50,null=True,blank=True)
    table13_00 = models.CharField(max_length=50,null=True,blank=True)
    table13_30 = models.CharField(max_length=50,null=True,blank=True)
    table14_00 = models.CharField(max_length=50,null=True,blank=True)
    table14_30 = models.CharField(max_length=50,null=True,blank=True)
    table15_00 = models.CharField(max_length=50,null=True,blank=True)
    table15_30 = models.CharField(max_length=50,null=True,blank=True)
    table16_00 = models.CharField(max_length=50,null=True,blank=True)
    table16_30 = models.CharField(max_length=50,null=True,blank=True)
    table17_00 = models.CharField(max_length=50,null=True,blank=True)
    table17_30 = models.CharField(max_length=50,null=True,blank=True)
    table18_00 = models.CharField(max_length=50,null=True,blank=True)
    table18_30 = models.CharField(max_length=50,null=True,blank=True)
    table19_00 = models.CharField(max_length=50,null=True,blank=True)
    table19_30 = models.CharField(max_length=50,null=True,blank=True)
    table20_00 = models.CharField(max_length=50,null=True,blank=True)
    table20_30 = models.CharField(max_length=50,null=True,blank=True)



    def __str__(self):
        return self.student_code