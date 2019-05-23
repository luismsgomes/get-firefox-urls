==================
 get_firefox_urls
==================

Copyright 2019 Luís Gomes <luismsgomes@gmail.com>.

``get_firefox_urls`` is a trivial Python module that implements a single convenience
function ``get_firefox_urls(mozilladir="~/.mozilla")`` that returns an iterator
of (w, t, url) tuples, where w and t are 0-based indexes of the window and tab and
url is the page URL.

By installing this package a command line script named get-firefox-urls is installed.
