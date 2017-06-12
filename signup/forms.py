from django import forms

from .models import Player

class PlayerForm(forms.ModelForms):

    class Meta:
        model = Player
        fields = ('first name', 'last name')
