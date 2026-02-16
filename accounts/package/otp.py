import random

def otp_generate():
  
  return ''.join(str(random.randint(0,9)) for _ in range(6))