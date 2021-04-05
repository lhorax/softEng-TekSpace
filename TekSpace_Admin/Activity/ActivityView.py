from django.shortcuts import render,redirect
from django.contrib import messages
from .Activity import *
from .ActivityForm import ActivityForm
from django.views.generic import View

# Create your views here.
class ActivityView(View):
    def index(request):
        return render(request, 'Activity/Activity.html')

    def activity_create(request):
        if request.method == 'POST':
            if 'addActivityBtn' in request.POST:
                form = ActivityForm(request.POST, files=request.FILES)
                if form.is_valid():
                    name = form.getName()
                    desc = form.getDescription()
                    venue = form.getVenue()
                    date = form.getDate()
                    photo = ''
                    if request.FILES.get('act_photo',False) != False:
                        photo = form.getPhoto()
                    interests = form.getInterests()
                    Activity.addActivity(name, desc, venue, date, photo, interests)
                    messages.success(request, ("Activity Successfully Added"))
                else:
                    print(form.errors)
                    messages.success(request, ("Sorry, there was an error making the activity"))
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
        if request.method == 'POST':
            if 'updateActivityBtn' in request.POST:
                obj = request.POST.get('name')
                activity = Activity.getActivity(obj)
                form = ActivityForm(request.POST, files=request.FILES, instance=activity)
                if form.is_valid():
                    name = form.getName()
                    desc = form.getDescription()
                    venue = form.getVenue()
                    date = form.getDate()
                    photo = ''
                    if request.FILES.get('act_photo',False) != False:
                        photo = form.getPhoto()
                    interests = form.getInterests()
                    Activity.updateActivity(obj,name,desc,venue,date,photo,interests)
                    messages.success(request, ("Activity Successfully Updated"))
                    return redirect('Activity:activity_view', name = name)
                else:
                    print(form.errors)
                    messages.success(request, ("Sorry, there was an error updating the activity"))
                    return redirect('Activity:activity_view', name = obj)

    def activity_delete(request):
        if request.method == 'POST':
            if 'deleteActivityBtn' in request.POST:
                form = ActivityForm(request.POST or None)
                id = form.getId()
                Activity.deleteActivity(id)
                messages.success(request, ("Activity Successfully Deleted"))
        return redirect('Social_Network:index_view')
        