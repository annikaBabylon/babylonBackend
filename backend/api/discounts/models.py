from django.db import models
from django.contrib.auth.models import User
from api.memberships.models import Membership

class Discount(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    percentage = models.IntegerField(blank=True, default=0)
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)
    cover_image = models.URLField(blank=True)
    required_membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return self.title

class UserDiscountActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    activation_date = models.DateTimeField(auto_now_add=True)