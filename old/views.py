from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!')

from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {})

def elaborate_html(request):
    return render(request, 'elaborate.html', {})

from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"