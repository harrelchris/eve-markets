from django.urls import path

from . import views

app_name = "sso"

urlpatterns = [
    path(route="authorize/", view=views.AuthorizeView.as_view(), name="authorize"),
    path(route="callback/", view=views.CallbackView.as_view(), name="callback"),
    path(route="logout/", view=views.LogoutView.as_view(), name="logout"),
]
