from django.urls import path
from .views import membership_list, membership_detail, purchased_membership_list, purchased_membership_detail

urlpatterns = [
    path('', membership_list, name='membership-list'),
    path('<int:pk>/', membership_detail, name='membership-detail'),
    path('purchased_memberships/', purchased_membership_list, name='purchased-membership-list'),
    path('purchased_memberships/<int:pk>/', purchased_membership_detail, name='purchased-membership-detail')
]