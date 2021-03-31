from django.db import models
from django.core.files import File
from django.core.validators import FileExtensionValidator
from .Module import Module

class File(models.Model):
    files = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    modules = models.ForeignKey(Module, on_delete=models.CASCADE)

    def getFiles(mod_ID):
       return File.objects.filter(modules_id=mod_ID)
    
    def createFiles(id, files):
        new_file = File()
        new_file.modules = Module.getModuleFile(id)
        new_file.files = files
        new_file.save()

    def removeFiles(id):
        query = File.objects.get(pk=id)
        query.delete()

    class Meta:
        db_table = "Files"




    
    
