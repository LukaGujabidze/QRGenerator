import os

def delete_file(file_name):
    file = file_name  
    location = f"/Users/lukgu/OneDrive/programing/QrCodeGenerator/static/qr/{file_name}" 
    os.remove(location)


    