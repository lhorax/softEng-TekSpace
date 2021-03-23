from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'Interest/Interest.html')

def interest_create(request):
    if request.method == 'POST':
        if 'addInterestBtn' in request.POST:
            form = InterestForm(request.POST, request.FILES)
            if form.is_valid():
                name = request.POST.get('int_name')
                desc = request.POST.get('int_description')
                photo = ''
                if request.FILES.get('int_photo',False) != False:
                    photo = request.FILES['int_photo']
                Interest.addInterest(name,desc,photo)
                messages.success(request, ("Interest Successfully Created"))
            else:
                print(form.errors)
                messages.success(request, ("Sorry, there was an error creating the activity"))
    return redirect('Social_Network:index_view')

def interest_view(request, name):
    interest = Interest.getInterest(name)
    context = {
        'interest':interest
    }
    return render(request, 'Interest/Interest.html',context)

def interest_update(request):
    if request.method == 'POST':
        obj = request.POST.get('name')
        if 'updateInterestBtn' in request.POST:
            interest = Interest.getInterest(obj)
            form = InterestForm(request.POST, request.FILES, instance=interest)
            if form.is_valid():
                name = request.POST.get('int_name')
                desc = request.POST.get('int_description')
                photo = ''
                if request.FILES.get('int_photo',False) != False:
                    photo = request.FILES['int_photo']

                Interest.updateInterest(obj,name,desc,photo)
                messages.success(request, ("Interest Successfully Updated"))
                return redirect('Interest:interest_view', name = name)
            else:
                print(form.errors)
                messages.success(request, ("Sorry, there was an error updating the interest"))
        return redirect('Interest:interest_view', name = obj)


def interest_delete(request):
    if request.method == 'POST':
        if 'deleteInterestBtn' in request.POST:
            id = request.POST.get('id')
            Interest.deleteInterest(id)
            messages.success(request, ("Interest Successfully Deleted"))
    return redirect('Social_Network:index_view')