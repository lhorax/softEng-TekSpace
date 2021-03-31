from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .Session import Session
from .SessionForm import SessionForm

# Create your views here.
class SessionsView(View):
       
    def viewSessions(request):
        context = {'sessions': Session.getSessions()}
        return render(request, 'Sessions/SessionsTemplate.html', context)

    def createSession(request):
        if request.method == 'POST':
            if 'addSessionBtn' in request.POST:
                form = SessionForm(request.POST or None)
                if form.is_valid():
                    code = form.getSessionCode()
                    name = form.getSessionName()
                    Session.addSession(code, name)
                    messages.success(request, ("Session Successfully Added"))
                else:
                    print(form.errors)
            
            return redirect("Sessions:index_view")
    
    def deleteSession(request):
        if request.method == 'POST':
            if 'deleteSessionBtn' in request.POST:
                form = SessionForm(request.POST or None)
                sid = form.getSessionId()
                Session.removeSession(sid)
                messages.success(request, ("Session Successfully Deleted"))     

            return redirect("Sessions:index_view")   

    def goToSessionPage(request):
        if request.method == 'POST':
            if 'viewSessionBtn' in request.POST:
                form = SessionForm(request.POST or None)
                sid = form.getSessionId()
                request.session['sid'] = sid

                return redirect("Modules:index_view")
        
    