import base64
import string
import random
from random import randint


tokens = []
base64_string = "=="
while(base64_string.find("==") != -1):
            sample_string = str(randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
            token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
                                                                                  
  

print(f"{token}")
