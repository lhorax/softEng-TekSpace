from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'Interest/Interest.html')

def interest_create(request):
    if 'addInterestBtn' in request.POST:
        form = InterestForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ("Interest Successfully Added"))
        else:
            print(form.errors)
    return redirect('Social_Network:index_view')

def interest_view(request, name):
    interest = Interest.objects.get(int_name = name)
    students = interest.students.all()
    context = {
        'interest':interest,
        'students':students
    }
    return render(request, 'Interest/Interest.html',context)

def interest_update(request):
    name = request.POST.get('name')
    if request.method == 'POST':
        if 'updateInterestBtn' in request.POST:
            interest = Interest.objects.get(int_name = name)
            form = InterestForm(request.POST, request.FILES, instance=interest)
            if form.is_valid():
                form.save()
                new_name = request.POST.get('int_name')
                return redirect('Interest:interest_view', new_name)
            else:
                print(form.errors)
    return redirect('Interest:interest_view', name = name)


def interest_delete(request):
    if request.method == 'POST':
        if 'deleteInterestBtn' in request.POST:
            id = request.POST.get('id')
            interest = Interest.objects.get(interest_id = id).delete()
            messages.success(request, ("Interest Successfully Deleted"))
    return redirect('Social_Network:index_view')
