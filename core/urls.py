from django.urls import path
from django.views import View

from django.urls import path
from users import views as user_views

app_name = "core"

urlpatterns = [
    path("", user_views.HomeView, name="home"),
]
