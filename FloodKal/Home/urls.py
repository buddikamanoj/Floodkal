from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'map', api.MapViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Map
    # url(r'^Home/map/$', views.MapListView.as_view(), name='Home_map_list'),
    # url(r'^Home/map/create/$', views.MapCreateView.as_view(), name='Home_map_create'),
    # url(r'^Home/map/detail/(?P<pk>\S+)/$', views.MapDetailView.as_view(), name='Home_map_detail'),
    # url(r'^Home/map/update/(?P<pk>\S+)/$', views.MapUpdateView.as_view(), name='Home_map_update'),

    url(r'^$', views.MapListView.as_view(), name='Home_map_list'),
    url(r'^about_us/$', TemplateView.as_view(template_name='about_us.html'), name="about_us"),



    url(r'^create/$', views.MapCreateView.as_view(), name='Home_map_create'),
    url(r'^detail/(?P<pk>\S+)/$', views.MapDetailView.as_view(), name='Home_map_detail'),
    url(r'^update/(?P<pk>\S+)/$', views.MapUpdateView.as_view(), name='Home_map_update'),

)
