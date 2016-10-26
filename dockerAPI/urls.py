from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /docker/
    url(r'^$', views.index, name='index'),
    # ex: /docker/images
    url(r'^images/$', views.images, name='images'),
    # ex: /docker/images/5basd34234
    #url(r'^(?P<image_id>[0-9]+)/$', views.image_detail, name='image_detail'),
    # ex: /docker/container/sdf098sdf89/
    #url(r'^(?P<container_id>[0-9]+)/results/$', views.container_detail, name='container_detail'),    
]