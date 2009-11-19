from django.db.models.fields import CharField

# TODO: We know what kind of data the user is entering. Should probably add a
# custom formfield.

class CountryField(CharField):
    def __init__(self, *args, **kwargs):
        from country_utils.countries import COUNTRY_CHOICES
        kwargs['max_length'] = 2
        kwargs['choices'] = COUNTRY_CHOICES
        kwargs['null'] = kwargs.get('null', False)
        CharField.__init__(self, *args, **kwargs)
