from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.user_list),
    path('<int:id>', views.user_detail)
]
