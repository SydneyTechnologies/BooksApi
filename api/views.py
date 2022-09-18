from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from . models import Book
from .serializers import BookSerializer

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