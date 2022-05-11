from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.AccountRegistration.as_view(), name='signup'),
    path('mypage/', views.mypage, name='mypage'),
    path('follow_to/', views.follow_to, name='follow_to'),
    path('follow_from/', views.follow_from, name='follow_from'),
    path('post/', views.post, name='post'),
    path('delete_save/<int:save_id>', views.delete_save, name='delete_save'),
    path('update_good/<int:outfit_id>/', views.update_good, name='update_good'),
    path('update_save/<int:outfit_id>/', views.update_save, name='update_save'),
    path('delete/<int:outfit_id>/', views.delete, name='delete'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('save/', views.save, name='save'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('<str:username>/', views.user_detail, name='user_detail'),
    path('<str:username>/<int:outfit_id>/', views.outfit_detail, name='outfit_detail'),
]
