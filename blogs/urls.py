from django.conf.urls import patterns, include, url


from blogs import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index)
)
