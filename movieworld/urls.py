from django.urls import path
from movieworld import views


app_name = 'movieworld'

urlpatterns = [
# add other urls here.


   path('/search', views.search, name='search'),
   path('/search/<query>/page/<page_no>', views.page, name='page'),
]