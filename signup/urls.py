from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.home, name='home'),
    url(r'^index/', views.index, name='index'),
    url(r'^registration/', views.registration, name='registration'),
]