from django.urls import path, include

from .views import LatestProductsList, ProductDetail, CategoryDetail, search, CategoryList, CommentList,\
    CommentProductList

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<slug:product_slug>/', CommentProductList.as_view()),
]