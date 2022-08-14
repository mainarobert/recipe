import imp
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/forgot_password.html', subject_template_name='user/password_reset_done.txt', html_email_template_name='users/password_reset_email.html'), name='password_reset'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='user/change_password.html'), name='change_pasword'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]