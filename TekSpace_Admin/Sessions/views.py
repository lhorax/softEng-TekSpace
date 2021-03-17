from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .models import Session
from .forms import SessionForm

# Create your views here.
class SessionsIndexView(View):
    def get(self, request):
        session_list = Session.objects.all
        context = {'sessions' : session_list}

        return render(request, 'Sessions/Sessions.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'addSessionBtn' in request.POST:
                form = SessionForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    messages.success(request, ("Session Successfully Added"))
                else:
                    print(form.errors)

            if 'deleteSessionBtn' in request.POST:
                sid = request.POST.get("session_id")
                query = Session.objects.get(pk=sid)
                query.delete()
                messages.success(request, ("Session Successfully Deleted"))

            if 'viewSessionBtn' in request.POST:
                messages.success(request, ("Session will redirect to another page"))

            session_list = Session.objects.all
            context = {'sessions' : session_list}

            return render(request, 'Sessions/Sessions.html', context)