from django import forms
from django.contrib.auth.models import User
from .models import Account, Flag, Outfit

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {
            'username':"ユーザーネーム",
            'email':"メールアドレス"
        }


class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = (
            'account_icon',
            'account_intro',
            )
        labels = {
            'account_icon':"プロフィール写真",
            'account_intro':"自己紹介",
            }


