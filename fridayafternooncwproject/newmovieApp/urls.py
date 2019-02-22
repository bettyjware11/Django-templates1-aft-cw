from django.urls import path

from . import views
# setting app routes
urlpatterns = [
    path('home/index/', views.index, name='index'),
    path('home/base/', views.base, name='base'),
    path('home/aboutpages/', views.aboutpages, name='aboutpages'),
    ]


