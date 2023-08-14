from django.urls import path, include

urlpatterns = [
    path('discounts/', include('discounts.urls')),
]