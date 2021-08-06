from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('follow_hook', views.follow_hook, name='follow_hook'),
    path('init', views.init, name='init'),
    path('signin', views.signin, name='signin'),
    path('close', views.close, name='close'),
    path('otp', views.otp, name='otp'),
]