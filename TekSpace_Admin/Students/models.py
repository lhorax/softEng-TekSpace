from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    id_number = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    bio = models.CharField(max_length=500, blank=True)
    is_loggedin = models.BooleanField(default=False)

    def __str__(self):
        return self.id_number + " " + self.user.first_name + " " + self.user.last_name

    class Meta:
        db_table = "Student"
    