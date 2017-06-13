from django.shortcuts import render
from django.template.context import RequestContext
from django.http import HttpResponse
from django.template import loader

from .models import DraftPod

def home(request):
    return render(request, 'signup/home.html')

def index(request):
    all_the_pods_for_this_week = DraftPod.objects
    context = {
        'all_the_pods_for_this_week' : all_the_pods_for_this_week
    }
    return render(request, 'signup/index.html', context)

def register(request):
    if request.method == 'POST':
        player = request.POST.get('player_name')
        draft_date = request.POST.get('draft_date')
        print(player)
        print(draft_date)
#        latest_available_pod = DraftPod.objects.last()
    return render(request, 'signup/register.html')

