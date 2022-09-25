from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from . models import Book
from .serializers import BookSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
# Create your views here.
class CreateBookApiView(CreateAPIView):
    # queryset is set to Book so drf knows what model to create with this endpoint
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class EditBookApiView(RetrieveUpdateAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer

class ListBookApiView(ListAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer

class DeleteBookApiView(DestroyAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

class LoginView(APIView):
    # this view will allow us to get our token in one of the following ways
    # through sending our login detail using a username and password (like signing in) 
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"Info":" Invalid credentials"})

        return Response({
            "Token": AuthToken.objects.create(user)[1]
        })
