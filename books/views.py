from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer
from .models import Books

# class BookListApiView(generics.ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def patch(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True, partial=True)
        return Response(serializer.data)
class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookApiViewset(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


