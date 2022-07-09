from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, authentication

from .models import Product, Category, Comment
from .serializers import ProductSerializer, CategorySerializer, CategoryListSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, category_slug, product_slug, format=None):
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get(self, request, category_slug, format=None):
        category = get_object_or_404(Category, slug=category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentProductList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    lookup_url_kwarg = "product_slug"

    def get_queryset(self):
        # category_slug = self.kwargs.get(self.lookup_url_kwarg[0])
        product_slug = self.kwargs.get(self.lookup_url_kwarg)
        comments = Comment.objects.filter(product__slug=product_slug)
        return comments

    def perform_create(self, serializer):
        product = Product.objects.get(slug=self.kwargs.get(self.lookup_url_kwarg))
        serializer.save(owner=self.request.user, product=product)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})



