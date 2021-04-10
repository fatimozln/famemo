from django.urls import path
from . import views

app_name = "profiles"
urlpatterns = [
    path('<user_id>/', views.profile_show, name="show"),
]
