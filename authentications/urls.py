from django.urls import path
from .views import register , login  , ProfileRetUpDesGenric

urlpatterns = [
    path("registration/", register , name="registration"),
    path("login/", login, name="signin"),
    # path("profile/", ProfileGenric.as_view(), name="profile"),
    path("profile/", ProfileRetUpDesGenric.as_view(), name="profile-update-delete"),
    # path("logout/", user_logout, name="logout"),
]