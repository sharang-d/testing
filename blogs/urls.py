from django.conf.urls import patterns, include, url
from blogs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>\d+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<blog_id>\d+)/$', views.edit, name='edit'),
    url(r'^update/(?P<blog_id>\d+)/$', views.update, name='update'),
    url(r'^destroy/(?P<blog_id>\d+)/$', views.destroy, name='destroy'),
)