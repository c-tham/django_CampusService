from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user$', views.user),
    url(r'^addUser$', views.addUser),
    url(r'^dashboard$', views.dashboard),
    url(r'^system$', views.system),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]
