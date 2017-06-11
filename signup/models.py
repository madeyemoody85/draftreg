from django.db import models
from django.utils import timezone

class DraftPod(models.Model):
    pod_number = models.IntegerField
    draft_date = models.DateField()
    player_count = models.IntegerField

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dci_number = models.CharField(max_length=15)
    draft_pod = models.ForeignKey(DraftPod, on_delete=models.CASCADE)
    