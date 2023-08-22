from django.urls import path, include

urlpatterns = [
    path('discounts/', include('api.discounts.urls')),
    path('users/', include('api.users.urls')),
    path('memberships/', include('api.memberships.urls')),
]