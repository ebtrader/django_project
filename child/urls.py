"""
URL configuration for helloworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from my_app import views
from .views import HomePageView


urlpatterns = [
    path('', views.hello_world, name='hello_world'),        # https://realpython.com/get-started-with-django-1/
    path('coolstuff', views.elaborate_html, name="elaborate"),
    path('nice', views.nice_html, name="nice_stuff"),
    path('test', HomePageView.as_view(), name="home"),      # https://djangoforbeginners.com/message-board/
    path("project", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
