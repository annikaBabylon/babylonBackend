from rest_framework import serializers
from .models import Membership, PurchasedMembership

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = [
            'pk',
            'name',
            'durationMonths',
            'price',
            'description'
        ]

class PurchasedMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedMembership
        fields = [
            'pk',
            'user',
            'membership',
            'purchase_date',
            'start_date',
            'end_date'
        ]