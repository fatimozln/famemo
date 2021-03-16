from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.articles_list, name='list'),
    path('add_post', views.add_post, name='add'),
    path('<slug>', views.articles_details, name='slug'),
    path('like/<postid>', views.like, name='like'),
    path('unlike/<postid>', views.unlike, name='unlike'),

]
