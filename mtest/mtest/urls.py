from django.conf.urls import patterns, url
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')

urlpatterns = patterns('',
    url(r'^$', home),
)
