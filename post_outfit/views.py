from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from post_outfit.models import Account, Outfit
from post_outfit.forms import OutfitForm, AccountForm, AddAccountForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    outfits = Outfit.objects.all()
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
        return redirect(to='/post_outfit/profile_edit')
    params = {
        'add_account_form': AddAccountForm(instance=add_account_obj)
    }
    return render(request, 'post_outfit/profile_edit.html', params)


@login_required
def mypage(request):
    return render(request, 'post_outfit/mypage.html')


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