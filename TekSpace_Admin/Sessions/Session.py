from django.db import models
from Students.Student import Student

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_code = models.CharField(max_length=20)
    session_name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.session_code + " " + self.session_name

    def getSessions():
        return Session.objects.all()
    
    def getSession(session_id):
        return Session.objects.get(pk = session_id)
    
    def addSession(code, name):
        new_session = Session()
        new_session.session_code = code
        new_session.session_name = name
        new_session.save()

    def removeSession(session_id):
        query = Session.objects.get(pk=session_id)
        query.delete()

    class Meta:
        db_table = "Session"
