from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from quotes.models import Quote

class QuoteCreate(CreateView):
    model = Quote

class QuoteUpdate(UpdateView):
    model = Quote

class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('quotes:index')
