from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from artikel.models import Artikel

def index(request):
    try:
        articles = Artikel.objects.order_by('-art_pub_date')[:10]
    except Artikel.DoesNotExist:
        articles = "No content available!"
        
    return render_to_response('index.html', {"articles":articles})

