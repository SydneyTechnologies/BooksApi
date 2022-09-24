from email.policy import default
from django.urls import path
from rest_framework import serializers
from . views import CreateBookApiView, EditBookApiView, ListBookApiView, DeleteBookApiView
from knox.views import LoginView, LogoutView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

class CustomLoginView(LoginView):
    permission_classes = [AllowAny,]
    # serializer_class = UserSerializer

urlpatterns = [
    path("create", CreateBookApiView.as_view(), name="create"),
    path("edit/<str:pk>", EditBookApiView.as_view(), name="edit"),
    path("list", ListBookApiView.as_view(), name="list"),
    path("delete/<str:pk>", DeleteBookApiView.as_view(), name="delete"),
    path("auth/login", CustomLoginView.as_view(), name="login"),
    path("auth/logout", LogoutView.as_view(), name="logout"),
]