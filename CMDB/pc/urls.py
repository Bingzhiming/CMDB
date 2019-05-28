"""CMDB06 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls  import url
from pc import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^add_service_type$', views.add_service_type, name='pc_add_service_type'),
    url('^service_types$', views.service_types, name='pc_service_types'),
    url('^add_system_type$', views.add_system_type, name='pc_add_system_type'),
    url('^system_types$', views.system_types, name='pc_system_types'),
    url('^add_oper$', views.add_oper, name='pc_add_oper'),
    url('^opers$', views.opers, name='pc_opers'),
    url('^add_pc$', views.add_pc, name='pc_add_pc'),
    url('^pcs$', views.pcs, name='pc_pcs'),
    url('^edit_pc$', views.edit_pc, name='pc_edit_pc')
]
