from django.urls import path

from .views import checkout, OrdersList, CurrentUser

urlpatterns = [
    path('checkout/', checkout),
    path('orders/', OrdersList.as_view()),
    path('current-user/', CurrentUser.as_view()),
]
