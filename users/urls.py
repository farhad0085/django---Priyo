from django.urls import path
from . import views as users_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', users_view.profile, name='profile'),
    path('login/', users_view.login_user, name='login'),
    path('register/', users_view.register_user, name='register'),
    path('logout/', users_view.logout_user, name='logout'),
    path('change-password/', users_view.change_password, name='change_password'),

    path('reset-password/',
        auth_views.PasswordResetView.as_view(template_name="users/reset/password-reset.html"),
        name='reset_password'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name="users/reset/password_reset_done.html"),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="users/reset/password_reset_confirm.html"),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="users/reset/password_reset_complete.html"),
        name='password_reset_complete'),

]
