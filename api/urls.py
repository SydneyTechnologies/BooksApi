from django.urls import path
from . views import CreateBookApiView, EditBookApiView, ListBookApiView, DeleteBookApiView
from .views import LoginView
from knox.views import LoginView as TokenView
from knox.views import LogoutView

urlpatterns = [
    # authentication urls
    path("auth/login", LoginView.as_view(), name="login"),
    path("auth/token", TokenView.as_view(), name="token"),
    path("auth/logout", LogoutView.as_view(), name="logout"),

    # api urls
    path("create", CreateBookApiView.as_view(), name="create"),
    path("edit/<str:pk>", EditBookApiView.as_view(), name="edit"),
    path("list", ListBookApiView.as_view(), name="list"),
    path("delete/<str:pk>", DeleteBookApiView.as_view(), name="delete"),

]