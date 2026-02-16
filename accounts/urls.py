from django.urls import path 
from .views import registrasi,verifikasi,success_registrasi,login_user

app_name = "accounts_app"
urlpatterns = [
  path('',login_user,name='login'),
  path('succes/',success_registrasi,name='succes'),
  path('verifikasi/<str:token>/',verifikasi,name='verifikasi'),
  path('registrasi/',registrasi,name='registrasi'),
  ]