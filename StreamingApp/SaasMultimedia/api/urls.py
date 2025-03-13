from django.urls import path
from .views import AddMultimedia, GetMultimedia

urlpatterns = [
    path("addmult/", AddMultimedia.as_view(), name="user_login"),
    path("getmult/<str:section>/", GetMultimedia.as_view(), name="user_login")
]