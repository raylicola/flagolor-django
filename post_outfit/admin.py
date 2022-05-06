from django.contrib import admin
from .models import Account, Flag, Outfit

# Register your models here.
admin.site.register(Account)
admin.site.register(Flag)
admin.site.register(Outfit)