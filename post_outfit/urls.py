from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.AccountRegistration.as_view(), name='signup'),
    path('admin_setting/', views.admin_setting, name='admin_setting'),
    path('mypage/', views.mypage, name='mypage'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('<str:username>/', views.user_detail, name='user_detail'),
    path('<str:username>/<int:outfit_id>/', views.outfit_detail, name='outfit_detail'),
]
