from django.urls import path
from . import views

urlpatterns = [
    path('health', views.HealthCheckView.as_view(), name='health'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]
