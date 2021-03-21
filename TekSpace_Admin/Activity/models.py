from django.db import models
from django.utils.timezone import now
from datetime import date
from Interest.models import Interest


# Create your models here.
class Activity(models.Model):
    activity_id     = models.AutoField(primary_key = True)
    act_name        = models.CharField(unique = True, max_length = 20)
    act_description = models.CharField(max_length = 100)
    act_photo       = models.FileField(default = 'default.png')
    act_venue       = models.CharField(max_length = 50)
    act_date        = models.DateTimeField(default = now)
    interests       = models.ManyToManyField(Interest, through='Activity_Interest', blank = True)

    class Meta:
        db_table = "Activity"
    
    def status(self):
        if self.act_date.date() > date.today():
            return "upcoming"
        elif self.act_date.date() == date.today():
            return "ongoing"
        else:
            return "closed"


class Activity_Interest(models.Model):
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['interest','activity']]
        db_table = "Activity_Interest"