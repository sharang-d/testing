from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib.auth import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', views.login, {'template_name': 'blogs/login.html'}, name='login'),
    url(r'^signup/$', 'blogs.views.signup', name='signup'),
    url(r'^logout/$', 'blogs.views.logout', name='logout'),
    url(r'^$', RedirectView.as_view(url='/blogs/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
)