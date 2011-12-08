=================
Hugsun Improved
=================

**Hugsun Improved** is a prototyp of `Hugsun <http://hugsun.org>`_ . It will base completly on *Django 
1.3.1*::

    from artikel.models import Artikel

    content = Artikel.objects.get(pk=1)

    render_to_response("/articles/index.html", {'artikel':content})


