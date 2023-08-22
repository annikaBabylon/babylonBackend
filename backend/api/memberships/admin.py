from django.contrib import admin
from .models import Membership, PurchasedMembership
# Register your models here.

admin.site.register(Membership)
admin.site.register(PurchasedMembership)