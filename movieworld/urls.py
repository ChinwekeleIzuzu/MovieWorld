
from django.urls import path
from movieworld import views

app_name = 'movieworld'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('login_check',views.login_check, name='login_check'),
    path('logout/', views.user_logout, name='logout'),
    path('movies', views.movies, name='movies'),
    path('search', views.search, name='search'),
    path('search/<query>/page/<page_no>/', views.page, name='page'),
    path('<imdb_id>', views.movieDetails, name='details'),
    path('<imdb_id>/review', views.review, name='reviews'),
    
]