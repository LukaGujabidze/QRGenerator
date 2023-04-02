import delete_qr
import time as t
from flask import Flask,render_template,request
import qrcode
import QRnm


app = Flask(__name__)


def make_qr(data):
    qr = qrcode.make(data)
    qrname = QRnm.make_name()
    qr.save(f"C:\\Users\\lukgu\\OneDrive\\programing\\QrCodeGenerator\\static\\qr\\{qrname}.png",format="PNG")
    full_qrname = f'{qrname}.png'
    return full_qrname

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home.html')
def index2():
    #delete_qr.delete_file('*')
    return render_template('home.html')


@app.route('/result.html',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      data = result.get('data')
      FILE_NAME = make_qr(data)
      file_name = str(FILE_NAME)

      return render_template("result.html",file_name = file_name)
   

if __name__ == '__main__':
   app.run(debug = True)   





