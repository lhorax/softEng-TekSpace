from django.db import models

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_code = models.CharField(max_length=20)
    session_name = models.CharField(max_length=50)

    def __str__(self):
        return self.session_code + " " + self.session_name

    class Meta:
        db_table = "Session"