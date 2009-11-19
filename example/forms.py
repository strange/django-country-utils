from django import forms

from example.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
