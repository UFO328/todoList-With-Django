import uuid
 
def token_generate() -> str:
  """
  membuat token url untuk link verifikasi
  otp 
  return string 
  """
  return str(uuid.uuid4())