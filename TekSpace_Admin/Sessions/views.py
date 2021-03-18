from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .models import Session
from .forms import SessionForm

# Create your views here.
class SessionsView(View):
    def get(self, request):
        context = self.updateTemplate()
        return render(request, 'Sessions/SessionsTemplate.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'addSessionBtn' in request.POST:
                form = SessionForm(request.POST or None)
                if form.is_valid():
                    self.createSession(request)
                    messages.success(request, ("Session Successfully Added"))
                else:
                    print(form.errors)

            if 'deleteSessionBtn' in request.POST:
                self.deleteSession(request)
                messages.success(request, ("Session Successfully Deleted"))

            if 'viewSessionBtn' in request.POST:
                self.goToSessionPage()
                messages.success(request, ("Session will redirect to another page"))

            context = self.updateTemplate()
            return render(request, 'Sessions/SessionsTemplate.html', context)
    
    def viewSessions(self):
        return Session.getSessions()

    def createSession(self, request):
        code = request.POST.get('session_code')
        name = request.POST.get('session_name')
        Session.addSession(code, name)
    
    def deleteSession(self, request):
        sid = request.POST.get("session_id")
        Session.removeSession(sid)

    def updateTemplate(self):
        return {'sessions' : self.viewSessions()}

    def goToSessionPage(self):
        pass
    