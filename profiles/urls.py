from django.urls import path
from . import views

app_name = "profiles"
urlpatterns = [
    path('<int:user_id>/', views.profile_show, name="show"),
    path('delete/<username>/', views.delete_user, name="delete"),
    path('deactive/', views.deactive_user, name="deactive"),
]
