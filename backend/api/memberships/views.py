from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Membership, PurchasedMembership
from .serializers import MembershipSerializer, PurchasedMembershipSerializer

class MembershipViewSet(viewsets.ViewSet):
    def list(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            membership = Membership.objects.get(pk=pk)
        except Membership.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    def create(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            membership = Membership.objects.get(pk=pk)
        except Membership.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MembershipSerializer(membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            membership = Membership.objects.get(pk=pk)
        except Membership.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

membership_list = MembershipViewSet.as_view({'get': 'list', 'post': 'create'})
membership_detail = MembershipViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})


class PurchasedMembershipViewSet(viewsets.ViewSet):
    def list(self, request):
        purchased_memberships = PurchasedMembership.objects.all()
        serializer = PurchasedMembershipSerializer(purchased_memberships, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            purchased_membership = PurchasedMembership.objects.get(pk=pk)
        except PurchasedMembership.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PurchasedMembershipSerializer(purchased_membership)
        return Response(serializer.data)

    def create(self, request):
        serializer = PurchasedMembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            purchased_membership = PurchasedMembership.objects.get(pk=pk)
        except PurchasedMembership.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PurchasedMembershipSerializer(purchased_membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            purchased_membership = PurchasedMembership.objects.get(pk=pk)
        except PurchasedMembership.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        purchased_membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

purchased_membership_list = PurchasedMembershipViewSet.as_view({'get': 'list', 'post': 'create'})
purchased_membership_detail = PurchasedMembershipViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})