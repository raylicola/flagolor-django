from django import forms
from django.contrib.auth.models import User
from post_outfit.models import Account, Flag, Outfit


class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {
            'username':"ユーザーネーム",
            'email':"メールアドレス"
        }


class AddAccountForm(forms.ModelForm):
    class Meta():
        model = Account
        fields = (
            'account_icon',
            'account_intro',
            )
        labels = {
            'account_icon':"プロフィール写真",
            'account_intro':"自己紹介",
            }


class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = (
            'outfit_photo',
            'outfit_desc',
            'outfit_good',
        )
