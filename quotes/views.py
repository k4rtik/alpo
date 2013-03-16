from django.shortcuts import render, get_object_or_404

from quotes.models import Quote

def index(request):
    latest_quote_list = Quote.objects.order_by('-submission_time')[:4]
    context = {'latest_quote_list': latest_quote_list}
    return render(request, 'quotes/index.html', context)

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/detail.html', {'quote':quote})
