from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='related_account'
        )

    # プロフィール写真
    account_icon = models.ImageField(
        upload_to="account_icon",
        default='account_icon/default.jpg',
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

    def __str__(self):
        return self.flag_name


class Outfit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='related_outfit'
        )
    flag = models.ForeignKey(
        Flag,
        on_delete=models.CASCADE,
        related_name='related_outfit'
        )
    outfit_photo = models.ImageField(upload_to="outfit_photo")
    outfit_desc = models.CharField(max_length=400)
    outfit_good = models.IntegerField(default=0)
    outfit_date = models.DateTimeField()


class Follow(models.Model):
    follow_to = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='related_follow_to'
        )
    follow_from = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='related_follow_from'
        )


class Save(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    outfit = models.ForeignKey(
        Outfit,
        on_delete=models.CASCADE,
        )