from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.user_list),
    #path('users/<int:id>', views.user_detail)

    #path('', views.discount_mixin_view, name='discount-list'),
    #path('<int:pk>/', views.discount_mixin_view, name='discount-detail'),
    #path('<int:pk>/update/', views.discount_update_api_view, name='discount-edit'),
    #path('<int:pk>/delete/', views.discount_delete_api_view),
]
