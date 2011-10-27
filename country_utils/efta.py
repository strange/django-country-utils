# Codes and information scraped (2011-10-28) from:
# http://epp.eurostat.ec.europa.eu/statistics_explained/index.php/Glossary:Country_codes

MEMBER_STATES = (
    'IS',
    'LI',
    'NO',
    'CH',
)

def is_member(iso_code, member_states=MEMBER_STATES):
    """Return a boolean indicating whether country represented by `iso_code`
    is a member of EFTA.

    >>> is_member('SE')
    False
    >>> is_member('IS')
    True

    """
    return iso_code in member_states

if __name__ == '__main__':
    import doctest
    doctest.testmod()
