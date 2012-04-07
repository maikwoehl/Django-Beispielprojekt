Hugsun Improved
=================

Name: Hugsun Improved
Version: v0.1rc2


Description
-----------
**Hugsun Improved** is a prototype of `Hugsun <http://hugsun.org>`_ . It will base completly on *Django 
1.3.1*::

    from artikel.models import Artikel

    content = Artikel.objects.get(pk=1)

    render_to_response("/articles/index.html", {'artikel':content})


The Standard Language is english.

Changelog
---------

**v0.1rc2**

* add category-tag with the art_tags to feed
* add tag view (example: http://my.domain/tagged/yourtag)
* remove box-shadow for the code-block
* add template block navigation
* remove category admin entry

**v0.1rc1**

* fix some css issues
* update design

**v0.1b2 beta 2**

* date format changed from "16 Dec 2011" to "16. Dec 2011"
* navigation-style add to site

**v0.1b beta**

* supports 2 format podcasts for crossbrowser html5 audio tag
* new template structure
* maybe you can use it for productive use, but wait until the final release is out(v0.1fr) 

**v0.1a alpha**

* Basic system
* Just one Podcast, but it is all what we have at this time

Version Concept
^^^^^^^^^^^^^^^

* for alpha versions we add an "a" at the end of the version.
* for beta version we add a "b" at the end of the version.
* for rc version we add a "rc" and the Release Candidate number at the end of version, like v0.1rc1
* for final release versions we add a "fr" at the end of the version
