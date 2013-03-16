from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def detail(request, quote_id):
    return HttpResponse("You're looking at quote %s." % quote_id)
