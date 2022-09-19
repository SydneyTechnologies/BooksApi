from django.urls import path
from . views import CreateBookApiView, EditBookApiView, ListBookApiView, DeleteBookApiView
urlpatterns = [
    path("create", CreateBookApiView.as_view(), name="create"),
    path("edit/<str:pk>", EditBookApiView.as_view(), name="edit"),
    path("list", ListBookApiView.as_view(), name="list"),
    path("delete/<str:pk>", DeleteBookApiView.as_view(), name="delete"),
]