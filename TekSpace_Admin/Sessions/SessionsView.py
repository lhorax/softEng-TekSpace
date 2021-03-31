from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .Session import Session
from .SessionForm import SessionForm

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
                    self.createSession(form)
                    messages.success(request, ("Session Successfully Added"))
                else:
                    print(form.errors)

            if 'deleteSessionBtn' in request.POST:
                form = SessionForm(request.POST or None)
                self.deleteSession(form)
                messages.success(request, ("Session Successfully Deleted"))

            if 'viewSessionBtn' in request.POST:
                form = SessionForm(request.POST or None)
                self.goToSessionPage(request, form)
                return redirect("Modules:index_view")

            context = self.updateTemplate()
            return render(request, 'Sessions/SessionsTemplate.html', context)
    
    def viewSessions(self):
        return Session.getSessions()

    def createSession(self, form):
        code = form.getSessionCode()
        name = form.getSessionName()
        Session.addSession(code, name)
    
    def deleteSession(self, form):
        sid = form.getSessionId()
        Session.removeSession(sid)

    def updateTemplate(self):
        return {'sessions' : self.viewSessions()}

    def goToSessionPage(self, request, form):
        sid = form.getSessionId()
        request.session['sid'] = sid
    