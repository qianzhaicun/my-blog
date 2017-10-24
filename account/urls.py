# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,logout_then_login

urlpatterns = [
    #url(r'^login/$',views.user_login,name='login'),
    # login / logout urls  
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', login, name='login'),
    #url(r'^logout/$',django.contrib.auth.views.logout,name='logout'),
    #url(r'logged_out/$',views.user_logout,name='logged_out'),  
    url(r'^logged_out/$',logout, {'template_name': 'registration/logged_out.html','next_page':'/account'},name='logged_out'),    
    url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),
]


