"""
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    # Prima della lezione 6 (=intro dei template)
    #return HttpResponse("<h1>The home page.</h1>")
    # Lezione 6: uso dei template
    return render(request, 'base.html')
"""
# New view for dynamic content:
from django.shortcuts import render

from . models import Page

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title':pg.title,
        'content':pg.bodytext,
        'last_update':pg.update_date,
    }
    # assert False
    return render(request, 'pages/page.html', context)
