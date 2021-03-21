from django.db import models
from Students.models import Student

# Create your models here.
class Interest(models.Model):
    interest_id     = models.AutoField(primary_key = True)
    int_name        = models.CharField(unique = True, max_length = 20)
    int_description = models.CharField(max_length = 300)
    int_photo       = models.FileField(default = 'default.png')
    students    = models.ManyToManyField(Student, blank=True)

    class Meta:
        db_table = "Interest"



