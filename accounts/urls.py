from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from . import views

# urlpatterns = [
#     path('login',views.user_login, name='login')
# ]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard_view, name='user-profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('signup/',views.user_register, name='signup'),
    path('profile/edit', views.edit_user, name='edit_profle')
]
