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
    account_introduction = models.TextField(
        blank=True,
        null=True,
        max_length=400,
        )

    def __str__(self):
        return self.user.username
