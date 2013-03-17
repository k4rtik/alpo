from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from quotes.models import Quote

from quotes import views

urlpatterns = patterns('',
        # ex: quotes/
        url(r'^$',
            ListView.as_view(
                queryset=Quote.objects.order_by('-submission_time')[:4],
                context_object_name='latest_quote_list',
                template_name='quotes/index.html'),
            name='index'),
        # ex: /quotes/2/
        url(r'^(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Quote,
                template_name='quotes/detail.html'),
            name='detail'),
)
