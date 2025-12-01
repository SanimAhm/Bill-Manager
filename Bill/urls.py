from django.urls import path
from .views import *

urlpatterns = [
    path("", BillView.as_view(), name='home'),
    path("register/", BillRegister.as_view(), name="register"),
    path("success/", success, name="success"),
]
