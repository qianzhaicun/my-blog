# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [          
    url(r'^$', views.students,name='students'),
    url(r'^add_student/', views.add_student),
    url(r'^del_student/', views.del_student),
    url(r'^edit_student/', views.edit_student),
    url(r'^test_ajax_list/', views.test_ajax_list),                
]


