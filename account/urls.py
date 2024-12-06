from django.urls import path
# Login👇
from django.contrib.auth.views import LoginView, LogoutView
# Password Reset 👇
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,  PasswordResetConfirmView ,  PasswordResetCompleteView

from account.views import profile_view, profile_edit

urlpatterns = [
    # Login👇
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    # Password Reset 👇
    path('reset/', PasswordResetView.as_view(), name ='password_reset'),
    path('resetDone/', PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('resetConfirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name = 'password_reset_confirm'),
    path('resetComplete/', PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
    # profile 👇
    path('profile/', profile_view, name= 'profile'),
    path('profile_edit/', profile_edit, name= 'profile_edit')
    # # profile edit ��
    # path('profile_edit/', edit_user, name= 'edit_user'),
    # # comment create/edit ��
    # path('comment_crete/', CommentEdit.as_view(), name='comment_crete'),
    # path('comment_edit', CommentDelete.as_view(), name='comment_edit')
]