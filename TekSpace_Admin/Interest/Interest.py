from django.db import models
from Students.Student import Student

# Create your models here.
class Interest(models.Model):
    interest_id     = models.AutoField(primary_key = True)
    int_name        = models.CharField(unique = True, max_length = 20)
    int_description = models.CharField(max_length = 300)
    int_photo       = models.FileField(default = 'default.png')
    students    = models.ManyToManyField(Student, blank=True)

    class Meta:
        db_table = "Interest"

    def addInterest(name, description, photo):
        try:
            new_interest = Interest()
            new_interest.int_name = name
            new_interest.int_description = description
            if photo != '':
                new_interest.int_photo = photo
            new_interest.save()
        except Exception as e:
            print(e)
    
    def updateInterest(obj, name, description, photo):
        if photo != '':
            interest = Interest.objects.get(int_name = obj)
            interest.int_name = name
            interest.int_description = description
            interest.int_photo = photo
            interest.save()
            # interest = Interest.objects.filter(int_name = obj).update(int_name = name, int_description = description, int_photo = photo)
        else:
            interest = Interest.objects.filter(int_name = obj).update(int_name = name, int_description = description)

    def deleteInterest(id):
        Interest.objects.get(interest_id = id).delete()

    def getInterestList():
        return Interest.objects.all()
    
    def getInterest(name):
        return Interest.objects.get(int_name = name)

    def getStudents(interest):
        return interest.students.all()

