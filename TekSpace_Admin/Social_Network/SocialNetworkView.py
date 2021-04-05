from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import date
from .SocialNetwork import *
from django.views.generic import View


# Create your views here.
class SocialNetworkView(View):
    def index(request):
        interest_list = Interest.getInterestList()
        today_activity = Activity.getTodayActivities()
        past_activity = Activity.getPastActivities()
        future_activity = Activity.getFutureActivities()

        context = {
            'interests':interest_list,
            'today_activity':today_activity,
            'past_activity':past_activity,
            'future_activity':future_activity,
        }

        return render(request, 'Social_Network/Social_Network.html', context)
