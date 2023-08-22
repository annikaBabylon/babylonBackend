from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    name = models.CharField(max_length=100)
    durationMonths = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class PurchasedMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    activate = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - " + self.membership.name