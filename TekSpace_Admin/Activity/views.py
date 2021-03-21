from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'Activity/Activity.html')

def activity_create(request):
    if request.method == 'POST':
        if 'addActivityBtn' in request.POST:
            form = ActivityForm(request.POST, files=request.FILES)
            if form.is_valid():
                name = request.POST.get('act_name')
                desc = request.POST.get('act_description')
                venue = request.POST.get('act_venue')
                date = request.POST.get('act_date')
                photo = ''
                if request.FILES.get('act_photo',False) != False:
                    photo = request.FILES['act_photo']
                interests = request.POST.getlist('interests')
                messages.success(request, ("Activity Successfully Added"))
            else:
                print(form.error)

                Activity.addActivity(name, desc, venue, date, photo, interests)
    return redirect('Social_Network:index_view')

def activity_view(request, name):
    activity = Activity.getActivity(name)
    tags = Activity.getTags(name)
    interests = Interest.getInterestList()
    context = {
        'activity':activity,
        'tags':tags,
        'interests':interests
    }
    return render(request, 'Activity/Activity.html',context)

def activity_update(request):
    # name = request.POST.get('name')
    obj = request.POST.get('name')
    if request.method == 'POST':
        if 'updateActivityBtn' in request.POST:
            form = ActivityForm(request.POST, files=request.FILES, instance=activity)
            if form.is_valid():
                name = request.POST.get('act_name')
                desc = request.POST.get('act_description')
                venue = request.POST.get('act_venue')
                date = request.POST.get('act_date')
                photo = ''
                if request.FILES.get('act_photo',False) != False:
                    photo = request.FILES['act_photo']
                interests = request.POST.getlist('interests')
                messages.success(request, ("Activity Successfully Updated"))
            else:
                print(form.errors)

            Activity.updateActivity(obj,name,desc,venue,date,photo,interests)
    return redirect('Activity:activity_view', name = name)
    

def activity_delete(request):
    if request.method == 'POST':
        if 'deleteActivityBtn' in request.POST:
            id = request.POST.get('id')
            Activity.deleteActivity(id)
            messages.success(request, ("Activity Successfully Deleted"))
    return redirect('Social_Network:index_view')
    