from django.urls import path

from . import views

app_name = "public"

urlpatterns = [
    path(route="", view=views.IndexView.as_view(), name="index"),
]
