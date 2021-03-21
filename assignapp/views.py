from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
def home(request):
    html="<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(html)
def index(request):
   return render(request,'index.html')
def shop(request):
   return render(request,'shop.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
class MyView(View):
    def get(self, request):
        return HttpResponse('This is a class based view 1')
class yourView(View):
    def get(self, request):
        return HttpResponse('This is a class based view 2')
class AboutView(TemplateView):
    template_name = "about.html"
class testview(TemplateView):
    template_name="test.html"