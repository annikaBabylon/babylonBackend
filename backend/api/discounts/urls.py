from django.urls import path
from . import views

urlpatterns = [
    path('', views.discount_mixin_view, name='discount-list'),
    path('<int:pk>/', views.discount_mixin_view, name='discount-detail'),
    path('update/<int:pk>', views.discount_update_api_view, name='discount-edit'),
    path('delete/<int:pk>', views.discount_delete_api_view),
]