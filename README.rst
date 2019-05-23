==================
 get_firefox_urls
==================

Copyright 2019 Luís Gomes <luismsgomes@gmail.com>, all rights reserved.


Installation
------------

.. code-block:: bash

    pip3 install get-firefox-urls

Usage from Python
-----------------

.. code-block:: python

    from get_firefox_urls import get_firefox_urls

    for w, t, url in get_firefox_urls():
        print("window %d tab %d: %s" % (w, t, url))

Usage from command line
-----------------------

.. code-block:: bash

    get-firefox-urls

Will output something like:

.. code-block::

    window 0 tab 0: https://github.com/luismsgomes/get-firefox-urls
    window 0 tab 1: https://pypi.org/project/get-firefox-urls/

License
-------

This software is licensed under the MIT license.

https://opensource.org/licenses/MIT
