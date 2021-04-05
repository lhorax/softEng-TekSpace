from django.db import models
from django.utils.timezone import now
from datetime import date
from Interest.Interest import Interest


# Create your models here.
class Activity(models.Model):
    activity_id     = models.AutoField(primary_key = True)
    act_name        = models.CharField(unique = True, max_length = 20)
    act_description = models.CharField(max_length = 300)
    act_photo       = models.FileField(default = 'default.png')
    act_venue       = models.CharField(max_length = 50)
    act_date        = models.DateTimeField(default = now)
    interests       = models.ManyToManyField(Interest, through='Activity_Interest', blank = True)

    class Meta:
        db_table = "Activity"
    
    def addActivity(name, desc, venue, date, photo, interests):
        new_act = Activity()
        new_act.act_name = name
        new_act.act_description = desc
        new_act.act_venue = venue
        new_act.act_date = date
        if photo != '':
            new_act.act_photo = photo
        new_act.save()

        for i in interests:
            interest = Interest.objects.get(interest_id = i)
            new_act.interests.add(interest)

        
    def updateActivity(obj, name, desc, venue, date, photo, interests):
        act = Activity.objects.get(act_name = obj)
        act.act_name = name
        act.act_description = desc
        act.act_venue = venue
        act.act_date = date
        
        if photo != '':
            act.act_photo = photo

        act.interests.clear()

        for i in interests:
            interest = Interest.objects.get(interest_id = i)
            act.interests.add(interest)
        act.save()

 
    def deleteActivity(id):
        Activity.objects.get(activity_id = id).delete()
    
    def getActivity(name):
        return Activity.objects.get(act_name = name)

    def getActivitityList():
        return Activity.objects.all()

    def getTags(name):
        activity = Activity.objects.get(act_name = name)
        return activity.interests.all()
    
    def status(self):
        if self.act_date.date() > date.today():
            return "upcoming"
        elif self.act_date.date() == date.today():
            return "ongoing"
        else:
            return "closed"
    def getTodayActivities():
        return Activity.objects.filter(act_date__date = date.today())
    def getPastActivities():
        return Activity.objects.filter(act_date__date__lt = date.today())
    def getFutureActivities():
        return Activity.objects.filter(act_date__date__gt = date.today())


class Activity_Interest(models.Model):
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['interest','activity']]
        db_table = "Activity_Interest"