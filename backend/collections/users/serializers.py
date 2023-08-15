from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id", 
            "username", 
            "first_name", 
            "last_name", 
            "email", 
            "password", 
            "country", 
            "city", 
            "profile_picture", 
            "creation_date", 
            "last_updated_date"
        ]