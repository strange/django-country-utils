from django.db import models

from country_utils.fields import CountryField

class Profile(models.Model):
    country1 = CountryField(blank=True)
    country2 = CountryField(blank=False, default='SE')
    country3 = CountryField(blank=False)
