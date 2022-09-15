from django.urls import path
from . import views

#urlpatterns = [
#    path('', views.index, name="index"),
#]

urlpatterns = [
    path('', views.index, {'pagename' : ''}, name="index"),
    #path('createvm', views.createvm, {'pagename' : 'createvm'}, name='createvm'),
    #path('deletevm', views.deletevm, {'pagename' : 'deletevm'}, name='deletevm'),
    #path('showvm', views.showvm, {'pagename' : 'showvm'}, name='showvm'),
    #path('loadkey', views.loadkey, {'pagename' : 'loadkey'}, name='loadkey'),
    #path('<str:pagename>', views.index, name='index'),
]

