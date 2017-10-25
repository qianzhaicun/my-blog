# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,logout_then_login,password_change,password_change_done

urlpatterns = [
    #url(r'^login/$',views.user_login,name='login'),
    # login / logout urls  
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', login, name='login'),
    #url(r'^logout/$',django.contrib.auth.views.logout,name='logout'),
    #url(r'logged_out/$',views.user_logout,name='logged_out'),  
    url(r'^logged_out/$',logout, {'template_name': 'registration/logged_out.html','next_page':'/account'},name='logged_out'),    
    url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),

    #change password urls
    #url(r'^password-change/$', password_change, {'template_name': 'registration/password_change_form.html'},name='password_change'),
    url(r'^password-change/$',views.password_change,name='password_change') ,   
    url(r'^password-change/done/$',views.password_change_done,name='password_change_done'),
]




