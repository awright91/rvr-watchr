from django import forms
from river_subs.models import RiverSubscription

class AddSubForm(forms.ModelForm):

    class Meta():
        model = RiverSubscription
        fields = ('trigger_level',)
