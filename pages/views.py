# New view for dynamic content:
from django.shortcuts import render

from . models import Page
#from . forms import CreatevmForm

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title':pg.title,
        'content':pg.bodytext,
        'last_update':pg.update_date,
        'page_list': Page.objects.all(),

    }
    #assert False
    return render(request, 'pages/page.html', context)
"""
def createvm(request, pagename):
    submitted=False
    if request.method == 'POST':
        form = CreatevmForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/createvm?submitted=True')
    else:
        form = CreatevmForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/createvm.html', {'createvmform': form, 'submitted': submitted})


def deletevm(request):
    submitted=False

def showvm(request):
    submitted=False

def loadkey(request):
    submitted=False
"""

