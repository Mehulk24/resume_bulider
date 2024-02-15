from django.utils import timezone
import os
import smtplib
from docx2pdf import convert
from PIL import Image
from io import BytesIO
from django.core.files import File
import random
from django.utils import timezone
import pdf2image
from docx2pdf import convert
from django.db.models import Count
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login   
from django.contrib import messages
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from resume.models import (
     
     User_t,
     Company,
     job_vacancy,
     apply_job,
     templates

)
import re
from docx import Document
from resume_bulider import settings

# Create your views here.
def navbar(request):
     return render(request,'navbar.html',{'email':request.session.get('email')});

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
               messages.error(request,"Invalid username or password")
               return redirect('login')
     return render(request,'login.html');

def sing_up(request):
     
     def otp_ver(email):

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
               user2 = User_t(username=user1,firstname=firstname,lastname=lastname,email=email,password=password,qualification="null")
               user2.save()
               login(request,user1)
               return redirect('/')
     return render(request,'email.html',{'otp':otp,'email':email});


def company(request):
     
     def otp_ver(email):
          

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

          if Company.objects.filter(c_name=cname).exists() or Company.objects.filter(c_email=cemail).exists():
               messages.error(request,"email or name is already exist plese login or try another email")
          elif len(cpassword)<8 :
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
          
          user = authenticate(username=cemail,password=cpassword)
          
          if user is not None:
               login(request,user)
               return redirect('c_home')
          else:
               messages.error(request,"email or password is wrong")
               return render(request,'company_login.html')
               
     return render(request,'company_login.html',)


def c_email(request):
     #company
     cootp=request.session.get('cootp')
     cname = request.session.get('cname')
     cemail = request.session.get('cemail')
     cpassword = request.session.get('cpassword')
     city = request.session.get('city')
     
     if request.method == 'POST':
          su = request.POST.get('pav')
          print(su)
          if su == '1':
               user = User.objects.create_user(username=cemail,email=cemail,password=cpassword,first_name=cname)
               cdata = Company.objects.create(c_name=cname,c_email=user,c_password=cpassword,c_location=city)
               user.save()
               cdata.save()  
               
               login(request,user) 
               return redirect('c_home')
          
          
          
     return render(request,'c_email.html',{'cootp':cootp,'cemail':cemail});


def profile(request):
     user_t = User_t.objects.get(username=request.user)
     print(request.user)
     print(User_t.u_img)
     con={
          'user_t':user_t
     }
     return render(request,'profile.html',con);

def edit_profile(request):
     user_t = User_t.objects.get(username=request.user)
     if request.method == 'POST':
          if 'u_img' in request.FILES:
               u_img = request.FILES['u_img']
          else:
               u_img = user_t.u_img
          firstname = request.POST['first_name']
          lastname = request.POST['lname']
          profession = request.POST['profession']
          website = request.POST['website']
          instrgram = request.POST['instrgram']
          linkdin = request.POST['linkdin']
          user = User.objects.get(username=request.user)
          user_t = User_t.objects.get(username=request.user)
          user.first_name = firstname
          user.last_name = lastname
          user.save()
          user_t.firstname = firstname
          user_t.lastname = lastname
          user_t.profession = profession
          user_t.website = website
          user_t.instrgram = instrgram
          user_t.linkdin = linkdin
          user_t.u_img = u_img
          user_t.save()
          messages.success(request, "Profile Updated Successfully")
          return redirect('profile')
     return render(request,'edit_profile.html',{'user_t':user_t});

def template(request):
     
     template = templates.objects.all()
     
     
     return render(request,'template.html',{'template':template});
          

def cerate_resume(request,t_id):
     

     def myreplace(document, replacements):
          for p in document.paragraphs:
               for t, r in replacements:
                    p.text = re.sub(t, r, p.text)

          for table in document.tables:
               for row in table.rows:
                    for cell in row.cells:
                         for t, r in replacements:
                              cell.text = re.sub(t, r, cell.text)

     replacements = [
     ("JOB TITLE", "Web Development"),
     ("INSTITUTION NAME", "GLS UNIVERSITY"),
     # Add more tuples here for additional replacements
     ]

     file = "resume.docx"
     document = Document(file)
     myreplace(document, replacements)
     document.save("demo1.docx")
     print("done")
     
     
     return render(request,'cerate_resume.html');

def job(request):
     
     
     job = job_vacancy.objects.all()
     
     j={
          'job':job,
     }
    
     return render(request,'job.html',j);

def job_details(request,jv_id):
     job = job_vacancy.objects.filter(jv_id=jv_id)
     j={
          'job':job,
     }
     return render(request,'jobs_details.html',j);

def my_logout(request):
    logout(request)
    
    return redirect('index')



def c_home(request):
     
     return render(request,'c_home.html');

def a_dasbord(request):
     c_u=User_t.objects.all().count()
     c_c=Company.objects.all().count()
     c_t=templates.objects.all().count()
     c_j=apply_job.objects.all().count()
     
     labels = ['Users', 'Companies', 'Jobs', 'Templates']
     data = [c_u, c_c, c_j, c_t]
     return render(request,'admin/dashboard.html',{'c_u':c_u,'c_c':c_c,'c_j':c_j,'c_t':c_t,'labels': labels, 'data': data});

def table(request):
     user = User_t.objects.all()
     company = Company.objects.all()
     job = job_vacancy.objects.all()
     apply = apply_job.objects.all()
     template = templates.objects.all()
     
     return render(request,'admin/tables.html',{'user':user,'company':company,'job':job,'apply':apply,'template':template});

def u_deletes(request,user_id=None):
     if user_id != None:
          user = User_t.objects.get(user_id=user_id)
          user.delete()
          return redirect("table")

          
     else:
          return render(request,"admin/table.html")
     
def c_deletes(request,c_id=None):
     
     if c_id != None:
          company = Company.objects.get(c_id=c_id)
          company.delete()
          return redirect("table")

          
     else:
          return render(request,"admin/table.html")
     
def j_deletes(request,jv_id=None):
     if jv_id != None:
          job = job_vacancy.objects.get(jv_id=jv_id)
          job.delete()
          return redirect("table")

     else:
          return render(request,"admin/table.html")
     
def t_deletes(request,t_id=None):
     if t_id != None:     
          template = templates.objects.get(t_id=t_id)
          template.delete()
          return redirect("table")
          
     else:
          return render(request,"admin/table.html")
     
     
     
     
     

def upload_templates(request):
     if request.method == 'POST':
          pdf = request.FILES['pdf']
          f_name = os.path.splitext(pdf.name)[0]
          template = templates(t_name=f_name,t_file=pdf)
          template.save()
          
          #pdf to image
          with open('temp.docx', 'wb+') as destination:
            for chunk in pdf.chunks():
                destination.write(chunk)

          subprocess.run(['unoconv', '-f', 'pdf', 'temp.docx'])

          images = pdf2image.convert_from_path('temp.pdf')

          image_io = BytesIO()
          images[0].save(image_io, format='PNG')

          my_model = templates.objects.get(t_name=f_name)  # replace with your actual model
          my_model.t_img.save(f'{f_name}.png', File(image_io), save=True)
          
          os.remove('temp.docx')
          os.remove('temp.pdf')

       
               
          messages.success(request, "Template Upload Successfully")
                    
          
   
     return render(request,'admin/upload_templates.html');



def admin_login(request):
     logout(request)
     
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request, user)
               if user.is_staff:
                    return redirect('a_dasbord')
               else:
                    return redirect('home')
          else:
               messages.error(request, "Invalid username or password")

  
     return render(request, 'admin/login.html')     
     
     
def post_job(request):
     if request.POST:
          job_title = request.POST['title']
          job_category = request.POST['category']
          time = request.POST['time']
          job_location = request.POST['location']
          city = request.POST['city']
          pin = request.POST['pin']
          job_salary = request.POST['salary']
          experience = request.POST['experience']
          job_function = request.POST['function']
          job_summary = request.POST['summary']
          job_key = request.POST['key']
          job_requirements = request.POST['requirements']
          c_id = Company.objects.get(c_email=request.user)
          
          print(job_title, job_category, job_location, job_salary, experience, job_function, job_summary, job_key, job_requirements)
          jv = job_vacancy.objects.create(jv_name=job_title,jv_category=job_category,jv_time=time,jv_location=job_location,jv_city=city,jv_pincode=pin,jv_salary=job_salary,jv_exprince=experience,jv_function=job_function,jv_description=job_summary,jv_key_responsibilites=job_key,jv_requirements=job_requirements,c_id=c_id)
          jv.save()
          
          con={
               "job": "job post successfully"
          }
          
          return render(request,'post_job.html',con)
          
     return render(request,'post_job.html')
          


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    request.user.last_activity = timezone.now()
    request.user.save()




