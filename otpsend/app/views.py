# from django.shortcuts import render
# from django.conf import settings
# from django.core.mail import send_mail
# def index(request):
#     subject = 'welcome to GFG world'
#     message = 'Hii i am Anushree. I am Full Stack Developer.How can i help you!..'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list=['anushreej537@gmail.com']
#     # recipient_list = ['py59681@gmail.com']
#     send_mail( subject, message, email_from, recipient_list )
#     return render(request,'index.html')

from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
import random
def index(request):
    return render(request,'index.html')

def sendemail(email,otp):
    subject = 'welcome to GFG world'
    message = f'YOUR OTP IS {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list=['anushreej537@gmail.com']
    # recipient_list = ['py59681@gmail.com']
    send_mail( subject, message, email_from, recipient_list )

def generateotp():
    return random.randint(100000,999999)

def sendotp(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generateotp()
        print(email)
        sendemail(email,otp)
        request.session['user_otp'] = otp
        return redirect('/varifyotp/')