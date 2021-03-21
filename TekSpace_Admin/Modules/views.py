from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.core.files import File
from django.http import FileResponse, Http404
from Sessions.models import Session
from .models import Modules, Files
from .forms import ModulesForm
from .forms import FilesForm

# Create your views here.
class ModulesView(View):
    def get(self, request):
        context = self.updateTemplate(request)
        return render(request, 'Modules/Session-Actions.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'addModulesBtn' in request.POST:
                form = ModulesForm(request.POST)
                if form.is_valid():
                    self.addModules(form, request)
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

            if 'goToSessionsPageBtn' in request.POST:
                return redirect("Sessions:index_view")

            context = self.updateTemplate(request)
            return render(request, 'Modules/Session-Actions.html', context)

    def addModules(self, form, request):
        sid = request.session.get('sid')
        session = Session.getSession(sid)
        name = form.cleaned_data['modulename']
        Modules.createModule(name, session)

    def addFiles(self, form, request):
        modID = request.POST.get('module_id')
        files = form.cleaned_data["files"]
        Files.createFiles(modID, files)

    def viewModules(self,request):
        sid = request.session.get('sid')
        return Modules.getModules(sid)
    
    def deleteModules(self, request):
        mid = request.POST.get("mod_ID")
        Modules.removeModules(mid)
    
    def deleteFiles(self, request):
        fid = request.POST.get("fileID")
        Files.removeFiles(fid)

    def updateTemplate(self,request):
        modules = self.viewModules(request)
        for mod in modules: 
            mod.files = Files.getFiles(mod.mod_ID)
        return {'modules': modules}

    


    


    

