from django.urls import path, include

urlpatterns = [
    path('discounts/', include('collections.discounts.urls')),
    path('users/', include('collections.users.urls'))
]