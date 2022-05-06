from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.AccountRegistration.as_view(), name='signup'),
    path('mypage/', views.mypage, name='mypage')
]
