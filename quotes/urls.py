from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from quotes.models import Quote

from quotes.views import QuoteCreate, QuoteUpdate, QuoteDelete

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
        #ex: /quotes/add/
        url(r'^add/$', QuoteCreate.as_view(
                template_name='quotes/form.html'),
            name='create'),
        #ex: /quotes/2/edit/
        url(r'^(?P<pk>\d+)/edit/$', QuoteUpdate.as_view(
                template_name='quotes/form.html'),
            name='update'),
        #ex: /quotes/2/delete/
        url(r'^(?P<pk>\d+)/delete/$', QuoteDelete.as_view(
                template_name='quotes/confirm_delete.html'),
            name='delete'),
)
