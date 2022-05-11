from django.contrib import admin
from .models import Account, Flag, Outfit, Follow, Save

# Register your models here.
admin.site.register(Account)
admin.site.register(Flag)
admin.site.register(Outfit)
admin.site.register(Follow)
admin.site.register(Save)