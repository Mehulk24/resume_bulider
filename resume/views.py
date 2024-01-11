from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.models import User
from resume.models import (
     
     User_t,
     compnay,
     job_vacancy,
     apply_job,
     templates

)

# Create your views here.
def index(request):
     return render(request,'index.html');


def hlogin(request):
     if request.method == 'POST':
          lusername = request.POST['lname']
          lpassword = request.POST['lpass']
          user = authenticate(username=lusername,password=lpassword)

          if user is not None:
               login(request,user)
               return redirect('index')
          else:
               return redirect('login')
     return render(request,'login.html');

def sing_up(request):
     
     def otp_ver(email):
          import smtplib
          import random
          from email.mime.text import MIMEText
          from email.mime.multipart import MIMEMultipart

          def generate_otp():
               digits = '0123456789'
               OTP = ''
               for i in range(6):
                    OTP += digits[random.randint(0, 9)]
               return OTP

          def send_email(sender_email, sender_password, receiver_email, subject, body):
               try:
                    # Connect to the SMTP server
                    smtp_server = 'smtp-mail.outlook.com'
                    port = 587
                    server = smtplib.SMTP(smtp_server, port)
                    server.starttls()

                    server.login(sender_email, sender_password)

                    message = MIMEMultipart()
                    message['From'] = sender_email
                    message['To'] = receiver_email
                    message['Subject'] = subject
                    message.attach(MIMEText(body, 'plain'))

                    # Send the email
                    server.sendmail(sender_email, receiver_email, message.as_string())
                    print("Email sent successfully!")

                    server.quit()

               except Exception as e:
                    print(f"Error: {e}")
          otp=generate_otp()
          request.session['otp'] = otp
          sender_email = 'resume.io.24@outlook.com'
          sender_password = 'vytbmfpufreksdvk'
          receiver_email = email
          subject = 'OTP to register in Resume Bulder'
          body = f'''Hi {request.session.get('fname')} 
          Wellcome to a Resume Bulder Website.
          Tank you For a Registrition To a site.
          Your Verification Code is : {otp}'''
          

          send_email(sender_email, sender_password, receiver_email, subject, body)
     
     if request.method == 'POST':
          username = request.POST['uname']
          firstname = request.POST['fname']
          lastname = request.POST['lname']
          email = request.POST['email']
          password = request.POST['password']
          
          if User_t.objects.filter(username=username).exists():
               messages.error(request, 'Username is already exist please try another username')
               
          elif User_t.objects.filter(email=email).exists():
               messages.error(request, 'Email is already exist please Login')
          
          elif len(password) < 8:
               messages.error(request,"password is too short,please enter more than 8 character")
               
          else:
               otp_ver(email)
               request.session['uname']= username
               request.session['fname']= firstname
               request.session['lname']= lastname
               request.session['email']= email
               request.session['password']= password
               
               return redirect('email')

     return render(request,'sing_up.html');

def email(request):
     otp=request.session.get('otp')
     username = request.session.get('uname')
     firstname = request.session.get('fname')
     lastname = request.session.get('lname')
     email = request.session.get('email')
     password = request.session.get('password')
     
    
     
     if request.method == 'POST':
          su = request.POST.get('pav')
          print(su)
          if su == '1':
               user1= User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
               user1.save()
               user2 = User_t(username=username,firstname=firstname,lastname=lastname,email=email,password=password,qualification="null")
               user2.save()
               
               return redirect('/login')
          
          
     return render(request,'email.html',{'otp':otp,'email':email});


def company(request):
     
     def otp_ver(email):
          import smtplib
          import random
          from email.mime.text import MIMEText
          from email.mime.multipart import MIMEMultipart

          def generate_otp():
               digits = '0123456789'
               OTP = ''
               for i in range(6):
                    OTP += digits[random.randint(0, 9)]
               return OTP

          def send_email(sender_email, sender_password, receiver_email, subject, body):
               try:
                    # Connect to the SMTP server
                    smtp_server = 'smtp-mail.outlook.com'
                    port = 587
                    server = smtplib.SMTP(smtp_server, port)
                    server.starttls()

                    server.login(sender_email, sender_password)

                    message = MIMEMultipart()
                    message['From'] = sender_email
                    message['To'] = receiver_email
                    message['Subject'] = subject
                    message.attach(MIMEText(body, 'plain'))

                    # Send the email
                    server.sendmail(sender_email, receiver_email, message.as_string())
                    print("Email sent successfully!")

                    server.quit()

               except Exception as e:
                    print(f"Error: {e}")
          otp=generate_otp()
          request.session['cootp'] = otp
          sender_email = 'resume.io.24@outlook.com'
          sender_password = 'vytbmfpufreksdvk'
          receiver_email = email
          subject = 'Resume Bulder Verification Code....'
          body = f'''Hello..! Wellcome to a Resume Bulder Website. \n Tank you For a Registrition To a site.\nYour Verification Code is : {otp}'''
          

          send_email(sender_email, sender_password, receiver_email, subject, body)
     
     if request.method == 'POST':
          cname = request.POST['cname']
          cemail = request.POST['cemail']
          cpassword = request.POST['cpassword']
          city = request.POST['city']
          
          if compnay.objects.filter(c_name=cname).exists() or compnay.objects.filter(c_email=cemail).exists():
               messages.error(request,"email is already exist plese login or try another email")
          elif cpassword >=8 :
               messages.error(request,"password is too short,please enter more than 8 character")
          else:
               otp_ver(cemail)
               request.session['cname']= cname
               request.session['cemail']= cemail
               request.session['cpassword']= cpassword
               request.session['city']= city
                    
               return redirect('/c_email')
          
          
    
     return render(request,'company.html');


def company_login(request):
     if request.method == 'POST':
          cemail = request.POST['cemail']
          cpassword = request.POST['cpassword']
     
     company_email = compnay.objects.all()
     company_password = compnay.objects.all()
        
     for i in range(len(company_email)):
          if cemail == company_email[i].c_email and cpassword == company_password[i].c_password:
               login(request,company_email[i])
               return redirect('/')
          else:
               print("not")
     
     return render(request,'company_login.html');


def c_email(request):
     #compnay
     cootp=request.session.get('cootp')
     cname = request.session.get('cname')
     cemail = request.session.get('cemail')
     cpassword = request.session.get('cpassword')
     city = request.session.get('city')
     
     if request.method == 'POST':
          su = request.POST.get('pav')
          print(su)
          if su == '1':
               cdata = compnay(c_name=cname,c_email=cemail,c_password=cpassword,c_location=city)
               cdata.save()
               return redirect('/')
          
          
          
     return render(request,'c_email.html',{'cootp':cootp,'cemail':cemail});


def profile(request):
     return render(request,'profile.html');

def template(request):
     return render(request,'template.html');

def job(request):
     return render(request,'job.html');

def my_logout(request):
    logout(request)
    
    return redirect('index')

def edit_profile(request):
     return render(request,'edit_profile.html');

