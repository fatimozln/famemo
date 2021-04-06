from django.urls import path
from . import views

app_name = "profiles"
urlpatterns = [
    path('<user>/', views.profile_show, name="show"),
]
