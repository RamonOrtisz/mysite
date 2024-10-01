from django.http import HttpResponse
from django.views.generic import generic

class PostView(generic.View):
def get(self, request, *args, **kwargs):
    return HttpResponse("Hello World")