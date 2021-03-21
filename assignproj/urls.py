"""assignproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from assignapp import views
from assignapp.views import MyView
from assignapp.views import yourView
from assignapp.views import AboutView
from assignapp.views import testview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('index',views.index),
    path('shop',views.shop),
    path('contact',views.contact),
    path('blog',views.blog),
    path('class1', MyView.as_view()),
    path('class2', yourView.as_view()),
    path('class3', AboutView.as_view()),
    path('class4',testview.as_view()),
]
