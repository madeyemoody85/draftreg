from django.shortcuts import render
from django.template.context import RequestContext
from django.http import HttpResponse
from django.template import loader

from .models import DraftPod, Player

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
        player_name = request.POST.get('player_name').split()
        date = request.POST.get('draft_date')

        try:
            # Date filter is wrong 
            draft_pod = DraftPod.objects.filter(draft_date=date)    # Get the last available for for the given date
        except DraftPod.DoesNotExist:
            draft_pod = None       # Create a new pod if one doesn't exist
            
        if draft_pod == None or draft_pod.player_count <= 0:
            draft_pod = DraftPod(draft_date=date, player_count=7)
        else:
            player_count = draft_pod.player_count - 1
            draft_pod.player_count = player_count

        #Save the drfat pod
        draft_pod.save()

        player = Player(first_name=player_name[0], last_name=player_name[1], draft_pod=draft_pod)
        player.save()

    return render(request, 'signup/register.html')

