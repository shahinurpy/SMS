from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.register_user , name='registration'),
    path("login/", views.login, name="signin"),
    path('otp/create/', views.create_otp),
    path('otp/verify/', views.verify_otp),
    path('password-reset/request/', views.request_password_reset),
    path('password-reset/confirm/', views.reset_password),
    path('password-change/', views.change_password),
]