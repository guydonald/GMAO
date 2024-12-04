from django.urls import path
from .views import register, login_user, home
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordChangeDoneView

urlpatterns = [
    path('register/', register, name='register'),
    path('change-password/', PasswordChangeView.as_view(template_name='authentication/change_password.html'), name='password-change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(template_name='authentication/change_password_done.html'), name='password-change-done'),
    path('login/', login_user, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
]
