from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^forgot/$', views.forgot, name='forgot'),
    url(r'^password/$', views.password, name='password'),
]