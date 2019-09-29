"""dj110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
#from . import api
from Home import views
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^$', views.MapListView.as_view(), name='Home_map_list'),
    #url(r'^about-us/$', TemplateView.as_view(template_name='Home/about-us.html')),
    #url(r'^foo/$', TemplateView.as_view(template_name='foo.html')),
    #url(r'^(?P<aboutus>)/$', 'Home.static', name='static'),
    #url(r'^about_us/$', views.about_us, name='about_us'),
    #url(r'^about_us/$', TemplateView.as_view(template_name='Home/templates/Home/about_us.html'), name="about_us"),
    url(r'^about-us/$', TemplateView.as_view(template_name='about_us.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact_us.html')),
    url(r'^History/$', TemplateView.as_view(template_name='history.html')),



    url(r'^admin/', admin.site.urls),
    url(r'^Home/', include('Home.urls')),
]
