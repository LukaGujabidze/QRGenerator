import random
import string

def make_name():
    first_qr_name = []
    
    for c in range(5):
        first_qr_name.append(random.choice(string.ascii_letters))

    qr_name = ''.join(first_qr_name)
    return(qr_name)
  