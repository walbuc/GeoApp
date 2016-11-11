from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^admin$', views.generateFiles, name='generateFiles'),
    url(r'^create/(?P<nombre>\w+)/(?P<apellido>\w+)/(?P<dni>\w+)$', views.createArbol,  name='createArbol'),
    url(r'^create/censista/(?P<nombre>\w+)/(?P<apellido>\w+)/(?P<dni>\w+)$', views.createCensita,  name='createCensista'),
]
