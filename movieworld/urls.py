from django.urls import path 
from movieworld import views

app_name = 'movieworld'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]