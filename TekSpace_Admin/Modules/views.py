from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.core.files import File
from django.http import FileResponse, Http404
from .models import Modules, Files
from .forms import ModulesForm
from .forms import FilesForm

# Create your views here.
class ModulesView(View):
    def get(self, request):
        context = self.updateTemplate()
        return render(request, 'Modules/Session-Actions.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'addModulesBtn' in request.POST:
                form = ModulesForm(request.POST)
                if form.is_valid():
                    self.addModules(form)
                    messages.success(request, ("Modules Successfully Added"))
                else:
                    print(form.errors)
            
            if 'addFileBtn' in request.POST:
                form = FilesForm(request.POST, request.FILES)
                if form.is_valid():
                    self.addFiles(form, request)
                    messages.success(request, ("File Successfully Added"))
                else:
                    print(form.errors)

            if 'deleteModulesBtn' in request.POST:
                self.deleteModules(request)
                messages.success(request, ("Modules Successfully Deleted"))
            
            if 'deleteFileBtn' in request.POST:
                self.deleteFiles(request)
                messages.success(request, ("File Successfully Deleted"))

            if 'viewModulesBtn' in request.POST:
                self.goToModulesPage()
                messages.success(request, ("Modules will redirect to another page"))

            context = self.updateTemplate()
            return render(request, 'Modules/Session-Actions.html', context)

    def addModules(self, form):
        name = form.cleaned_data['modulename']
        Modules.createModule(name)

    def addFiles(self, form, request):
        modID = request.POST.get('module_id')
        files = form.cleaned_data["files"]
        Files.createFiles(modID, files)

    def viewModules(self):
        return Modules.getModules()
    
    def deleteModules(self, request):
        mid = request.POST.get("mod_ID")
        Modules.removeModules(mid)
    
    def deleteFiles(self, request):
        fid = request.POST.get("fileID")
        Files.removeFiles(fid)

    def updateTemplate(self):
        modules = self.viewModules()
        for mod in modules: 
            mod.files = Files.objects.filter(modules_id=mod.mod_ID)
        return {'modules': modules}

    


    


    

