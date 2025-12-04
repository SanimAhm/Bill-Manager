from django.urls import path
from .views import *

urlpatterns = [
    path("", BillView.as_view(), name='home'),
    path("<int:pk>/", BillDetailView.as_view(), name="bill_detail"),
    path("register/", BillRegister.as_view(), name="register"),
    path("success/", success, name="success"),
]
