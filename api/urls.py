from django.urls import path
from . views import CreateBookApiView, EditBookApiView, ListBookApiView
urlpatterns = [
    path("create", CreateBookApiView.as_view(), name="create"),
    path("edit/<str:pk>", EditBookApiView.as_view(), name="edit"),
    path("list", ListBookApiView.as_view(), name="list"),
]