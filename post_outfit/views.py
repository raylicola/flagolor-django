from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from post_outfit.models import Account, Follow, Outfit, Save
from post_outfit.forms import OutfitForm, AccountForm, AddAccountForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    outfits = Outfit.objects.exclude(user=request.user)
    params = {
        'outfits': outfits,
    }
    return render(request, 'post_outfit/index.html', params)


def outfit_detail(request, outfit_id, username):
    outfit = Outfit.objects.get(id=outfit_id)
    account = Account.objects.get(user__username=username)
    params = {
        'account': account,
        'username': username,
        'outfit': outfit,

    }
    return render(request, 'post_outfit/outfit_detail.html', params)


def user_detail(request, username):
    if username==request.user.username:
        return render(request, 'post_outfit/mypage.html')
    else:
        account = Account.objects.get(user__username=username)
        outfits = Outfit.objects.filter(user__username=username)
        params = {
            'account': account,
            'outfits': outfits,
        }
        return render(request, 'post_outfit/user_detail.html', params)


@login_required
def profile_edit(request):
    add_account_obj = Account.objects.get(user__username=request.user.username)
    if (request.method=='POST'):
        add_account = AddAccountForm(request.POST, instance=add_account_obj)
        add_account.save()
    params = {
        'add_account_form': AddAccountForm(instance=add_account_obj)
    }
    return render(request, 'post_outfit/profile_edit.html', params)


@login_required
def save(request):
    saves = Save.objects.filter(user=request.user)
    params = {
        'saves': saves,
    }
    return render(request, 'post_outfit/save.html', params)


@login_required
def mypage(request):
    return render(request, 'post_outfit/mypage.html')


@login_required
def follow(request, username):
    follow_to = User.objects.get(username=username)
    follow_from = request.user
    if (len(Follow.objects.filter(follow_to=follow_to, follow_from=follow_from)) == 0):
        follow = Follow(follow_to=follow_to, follow_from=follow_from)
        follow.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required
def update_save(request, outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)
    user = request.user
    if (len(Save.objects.filter(user=user, outfit=outfit)) == 0):
        save = Save(user=user, outfit=outfit)
        save.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required
def update_good(request, outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)
    outfit.outfit_good += 1
    outfit.save()
    print(outfit.outfit_good)
    return redirect(request.META['HTTP_REFERER'])


class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"post_outfit/signup.html",context=self.params)

    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            if 'account_icon' in request.FILES:
                add_account.account_icon = request.FILES['account_icon']

            add_account.save()
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"post_outfit/signup.html",context=self.params)