from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.core.files import File
from django.http import FileResponse, Http404
from Sessions.Session import Session
from .Module import Module
from .File import File
from .ModuleForms import ModulesForm, FilesForm

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
                    messages.error(request, ("File Not Accepted! File must be in PDF Format."))

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
        name = form.getModuleName()
        Module.createModule(name, session)

    def addFiles(self, form, request):
        modules_form = ModulesForm(request.POST or None)
        modID = modules_form.getModuleID()
        files = form.getFiles()
        File.createFiles(modID, files)

    def viewModules(self,sid):
        return Module.getModules(sid)
    
    def deleteModules(self, request):
        form = ModulesForm(request.POST or None)
        mid = form.getModuleID()
        Module.removeModules(mid)
    
    def deleteFiles(self, request):
        file_form = FilesForm(request.POST or None)
        fid = file_form.getFileID()
        File.removeFiles(fid)

    def updateTemplate(self,request):
        sid = request.session.get('sid')
        session = Session.getSession(sid)
        modules = self.viewModules(sid)
        for mod in modules: 
            mod.files = File.getFiles(mod.mod_ID)
        return {'modules': modules, 'session': session }