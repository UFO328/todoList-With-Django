from django.core.mail import send_mail 
from django.conf import settings 
from .generate_token import token_generate
from ..models import OTP 
from .otp import otp_generate


def send_otp(user,request):
  
  token = token_generate()
  otp_code = otp_generate()
  OTP.objects.create(user=user,code=otp_code,token=token)
  link = f"http://{request.get_host()}/verifikasi/{token}/"  
  subject = 'OTP VERIFICATION'
  messages = f"HI {user.username} THIS YOUR OTP {otp_code}\nDONT SHOW TO ANOTHER PEOPLE\n PLEASE KLIK LINK FOR VERIFICATION OTP {link}"
  send_mail(subject,messages,settings.EMAIL_HOST_USER,[user.email])
  return token