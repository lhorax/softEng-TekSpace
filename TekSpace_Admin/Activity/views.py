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
                activity = form.save()
                messages.success(request, ("Activity Successfully Added"))
                int_list = request.POST.getlist('interests')
                for i in int_list:
                    interest = Interest.objects.get(interest_id = i)
                    activity.interests.add(interest)
            else:
                print(form.errors)
    return redirect('Social_Network:index_view')

def activity_view(request, name):
    activity = Activity.objects.get(act_name = name)
    tags = activity.interests.all()
    interests = Interest.objects.all()
    context = {
        'activity':activity,
        'tags':tags,
        'interests':interests
    }
    return render(request, 'Activity/Activity.html',context)

def activity_update(request):
    name = request.POST.get('name')
    if request.method == 'POST':
        if 'updateActivityBtn' in request.POST:
            activity = Activity.objects.get(act_name = name)
            form = ActivityForm(request.POST, files=request.FILES, instance=activity)
            if form.is_valid():
                activity = form.save()
                new_name = request.POST.get('act_name')
                return redirect('Activity:activity_view', name = new_name)
            else:
                print(form.errors)
    return redirect('Activity:activity_view', name = name)
    

def activity_delete(request):
    if request.method == 'POST':
        if 'deleteActivityBtn' in request.POST:
            id = request.POST.get('id')
            activity = Activity.objects.get(activity_id = id).delete()
            messages.success(request, ("Activity Successfully Deleted"))
    return redirect('Social_Network:index_view')
    