====================
Django Country Utils
====================

A dirty toss-in application I use to add a CountryField to Django projects.

Installation
============

Add ``country_utils`` to ``INSTALLED_APPS`` in your project's settings module.

You can now add a ``CountryField`` to your models::

    from country_utils.fields import CountryField

    class Profile(models.Model):
        country = CountryField()
        ...

Examples
========

There are some non-exhaustive examples in the application `example` located in
the root directory of the repository.

TODO
====

There's a lot to do to make this universally useful (sort country names by
their localized name, add translations, add a "short" name for countries that
require one etc). I add stuff as I need it. Feel free to contribute.
