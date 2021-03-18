from django.db import models

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_code = models.CharField(max_length=20)
    session_name = models.CharField(max_length=50)

    def __str__(self):
        return self.session_code + " " + self.session_name

    def getSessions():
        return Session.objects.all()
    
    def addSession(code, name):
        new_session = Session()
        new_session.session_code = code
        new_session.session_name = name
        new_session.save()

    def removeSession(id):
        query = Session.objects.get(pk=id)
        query.delete()

    class Meta:
        db_table = "Session"