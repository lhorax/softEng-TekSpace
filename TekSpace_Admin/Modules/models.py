from django.db import models
from django.core.files import File
from django.core.validators import FileExtensionValidator

# Create your models here.
class Modules(models.Model) :
    mod_ID = models.AutoField(primary_key=True)
    modulename = models.CharField(max_length=200)
    # files = models.Ma(Files, on_delete=models.CASCADE)

    def __str__(self):
        return self.modulename
    
    def createModule(modulename):
        new_module = Modules()
        new_module.modulename = modulename
        new_module.save()
    
    def getModules():
        return Modules.objects.all()
    
    def getModuleFile(id):
        return Modules.objects.get(pk=id)
        
    def removeModules(id):
        query = Modules.objects.get(pk=id)
        query.delete()

    class Meta:
        db_table = "modules"

class Files(models.Model):
    files = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    modules = models.ForeignKey(Modules, on_delete=models.CASCADE)

    def getFiles(mod_ID):
       return Modules.objects.get(modules_id=mod_ID)
    
    def createFiles(id, files):
        new_file = Files()
        new_file.modules = Modules.getModuleFile(id)
        new_file.files = files
        new_file.save()

    def removeFiles(id):
        query = Files.objects.get(pk=id)
        query.delete()

    class Meta:
        db_table = "files"




    
    
    



    

    
