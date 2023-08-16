from django.db import models

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    profile_picture = models.URLField(max_length=200, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
