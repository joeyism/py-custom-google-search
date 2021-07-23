
py-custom-google-search
=======================

This library is to ease with the usage of custom Google Search API. This means that you can use this library to programatically perform Google searches with the API, without the need for scraping (which means that it is much lighter).

Installation
------------

To install, run

.. code-block::

   pip install custom-google-search

Usage
-----

Getting CX Number and API Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow `this tutorial <https://joeyism.medium.com/custom-google-search-api-fbbafe4711eb>`_ on how to get your CX Number and API Key

Programmatically
^^^^^^^^^^^^^^^^

.. code-block:: python

   from custom_google_search import search
   search("nike logo", key=API_KEY, cx=CX_NUMBER)

where ``API_KEY`` and ``CX_NUMBER`` are the API Key and CX Number respectively.
