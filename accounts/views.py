from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .package import send_otp
from .models import OTP
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

def registrasi(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    
    #memeriksa apakah username sudah terdaftar
    if User.objects.filter(username=username).exists():
      messages.error(request,'USERNAME TIDAK TERSEDIA')
      return redirect('accounts_app:registrasi')
    
    #memeriksa apakah password sama dengan confirm password
    if confirm != password:
      messages.error(request,'PASSWORD TIDAK SAMA')
      return redirect('accounts_app:registrasi')
    
    #memeriksa apakah password panjang nya 8 character
    if len(password) <= 8:
      messages.error(request,'PASSWORD MINIMAL 8 CHARCTER')
      return redirect('accounts_app:registrasi')
    
    #create user dengan password yang sudsh langsung
    #di hash
    user = User.objects.create_user(
      username=username,
      email=email,
      password=password,
      is_active=False
      )
    
    send_otp(user,request)
    return redirect('accounts_app:succes')
  return render(request,'account/registrasi.html')

def verifikasi(request,token):
    if request.method == 'POST':
      otp_input = request.POST.get('otp')
      try:
        otp_obj = OTP.objects.get(token=token)
      except OTP.DoesNotExist:
        messages.error(request,'OTP IS NOT VALID AGAIN')
      user = otp_obj.user
      
      if not otp_obj.is_valid() :
        messages.error(request,'OTP IS EXPIRED')
        otp_obj.delete()
        return redirect('accounts_app:registrasi')
        
      if otp_obj.code == otp_input and otp_obj.is_valid():
        user.is_active = True 
        user.save()
        otp_obj.delete()
        messages.success(request,'OTP IS VALID')
        return redirect('accounts_app:login')
        
      if otp_obj.code != otp_input:
        messages.error(request,'OTP IS NOT VALID')
        return redirect('accounts_app:verifikasi',{'token':token})
      
    else:
      return render(request,'account/verifikasi_otp.html',{'token':token})
      
def success_registrasi(request):
  return render(request,'account/succes.html')

def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    #print("USERNAME:", username)
    #print("PASSWORD:", password)

    user = authenticate(request,username=username,password=password)
    
    if user and user.is_active:
      login(request,user)
      return redirect('task_app:task_page')
    else:
      messages.error(request,'USERNAME ATAU PASSWORD SALAH')
      return redirect('accounts_app:login')
  return render(request,'account/login.html')

@login_required
def log_out(request):
  logout(request)
  return redirect('accounts_app:login')