# Codes and information scraped (2011-10-28) from:
# http://epp.eurostat.ec.europa.eu/statistics_explained/index.php/Glossary:Country_codes

MEMBER_STATES = (
    'AT',
    'BE',
    'BG',
    'CY',
    'CZ',
    'DE',
    'DK',
    'EE',
    'EL',
    'ES',
    'FI',
    'FR',
    'HU',
    'IE',
    'IT',
    'LT',
    'LU',
    'LV',
    'MT',
    'NL',
    'PL',
    'PT',
    'RO',
    'SE',
    'SI',
    'SK',
    'UK', 
)

def is_member(iso_code, member_states=MEMBER_STATES):
    """Return a boolean indicating whether country represented by `iso_code`
    is a member of the EU.

    >>> is_member('SE')
    True
    >>> is_member(u'SE')
    True
    >>> is_member('US')
    False
    >>> is_member('JP')
    False

    """
    return iso_code in member_states

if __name__ == '__main__':
    import doctest
    doctest.testmod()
