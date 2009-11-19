tests = """

>>> profile = Profile.objects.create(country3='US')
>>> assert(profile.country1 == '')
>>> assert(profile.country2 == 'SE')
>>> assert(profile.country3 == 'US')

>>> data = { 'country1': 'GB', 'country2': 'SE', 'country3': 'US' }
>>> form = ProfileForm(data=data)
>>> form.is_valid()
True

>>> data = { 'country2': 'US' }
>>> form = ProfileForm(data=data)
>>> form.is_valid()
False

>>> form = ProfileForm()
>>> country1_choices = form.fields['country1'].choices
>>> country2_choices = form.fields['country2'].choices
>>> country3_choices = form.fields['country3'].choices
>>> assert(len(country1_choices) == len(country3_choices))
>>> assert(len(country2_choices) != len(country1_choices))
>>> assert(len(country2_choices) != len(country3_choices))

"""

from example.models import Profile
from example.forms import ProfileForm

__test__ = { 'doctest': tests }
