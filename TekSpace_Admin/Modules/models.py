from django.db import models
from django.core.files import File
from django.core.validators import FileExtensionValidator
from Sessions.Session import Session

# Create your models here.
class Module(models.Model) :
    mod_ID = models.AutoField(primary_key=True)
    modulename = models.CharField(max_length=50)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.modulename
    
    def createModule(modulename, session):
        new_module = Module()
        new_module.modulename = modulename
        new_module.session = session
        new_module.save()
    
    def getModules(sid):
        return Module.objects.filter(session_id=sid)
    
    def getModuleFile(id):
        return Module.objects.get(pk=id)
        
    def removeModules(id):
        query = Module.objects.get(pk=id)
        query.delete()

    class Meta:
        db_table = "Modules"

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




    
    
    



    

    
