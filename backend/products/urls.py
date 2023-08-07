from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_mixin_view, name='product-list'),
    path('<int:pk>/', views.product_mixin_view, name='product-detail'),
    path('<int:pk>/update/', views.product_update_api_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_delete_api_view),
]