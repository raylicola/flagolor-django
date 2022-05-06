from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # プロフィール写真
    account_icon = models.ImageField(
        upload_to="account_icon",
        blank=True,
        null=True
        )

    # 自己紹介文
    account_intro = models.TextField(
        blank=True,
        null=True,
        max_length=400,
        )

    def __str__(self):
        return self.user.username


class Flag(models.Model):
    flag_name = models.CharField(max_length=30)
    flag_image =  models.ImageField(upload_to="flag_image")
    flag_start_date = models.DateField()
    flag_end_date = models.DateField()


class Outfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
    outfit_photo = models.ImageField(upload_to="outfit_photo")
    outfit_desc = models.CharField(max_length=400)
    outfit_good = models.IntegerField(default=0)
