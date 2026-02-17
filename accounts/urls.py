from django.urls import path 
from .views import registrasi,verifikasi,success_registrasi,login_user,log_out

app_name = "accounts_app"
urlpatterns = [
  path('',login_user,name='login'),
  path('registrasi/',registrasi,name='registrasi'),
  path('logout/',log_out,name='logout'),
  path('verifikasi/<str:token>/',verifikasi,name='verifikasi'),
  path('succes/',success_registrasi,name='succes'),
  ]