from django.conf.urls import patterns, url
import django.contrib.auth.views
from login import views

urlpatterns = patterns('',
    url(r'^login/$', django.contrib.auth.views.login, name='login'),
    url(r'^profile/$', views.user_home, name='user_home'),
)