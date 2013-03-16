from django.conf.urls import patterns, url

from quotes import views

urlpatterns = patterns('',
        # ex: quotes/
        url(r'^$', views.index, name='index'),
        # ex: /quotes/2/
        url(r'^(?P<quote_id>\d+)/$', views.detail, name='detail'),
)
