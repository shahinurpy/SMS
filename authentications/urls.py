from django.urls import path
from .views import views


urlpatterns = [
    path('registration/', register_user , name='registration'),
    path("login/", login, name="signin"),
    path('otp/create/', views.create_otp),
    path('otp/verify/', views.verify_otp),
    path('password-reset/request/', views.request_password_reset),
    path('password-reset/confirm/', views.reset_password),
    path('password-change/', views.change_password),
]