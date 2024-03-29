from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_t(models.Model):
     user_id = models.AutoField(primary_key=True)
     username = models.OneToOneField(User,on_delete=models.CASCADE,to_field='username')
     firstname = models.CharField(max_length=50)
     lastname = models.CharField(max_length=50)
     qualification = models.CharField(max_length=50,default=" ")
     email = models.EmailField(max_length=50)
     password = models.CharField(max_length=50)
     website = models.CharField(max_length=100,default="")
     instrgram = models.CharField(max_length=100,default="")
     linkdin = models.CharField(max_length=100,default="")
     profession = models.CharField(max_length=100,default="")
     u_img = models.ImageField(upload_to='images/user/',default="images/user.png")
     u_resume = models.FileField(upload_to='u_resume/',default="")
     r_pdf = models.FileField(upload_to='r_pdf/',default="")
     r_img = models.ImageField(upload_to='img_r/',default="")
     r_qr = models.ImageField(upload_to='qr/',default="")
     
     def __str__(self):
          return self.firstname
     
     

class Company(models.Model):
     c_id = models.AutoField(primary_key=True)
     c_name = models.CharField(max_length=50,unique=True)
     c_email = models.OneToOneField(User,on_delete=models.CASCADE,to_field='username')
     c_password = models.CharField(max_length=50)
     c_location = models.CharField(max_length=50)
     website = models.CharField(max_length=100,default="")
     instrgram = models.CharField(max_length=100,default="")
     linkdin = models.CharField(max_length=100,default="")
     c_img = models.ImageField(upload_to='images/compnay/',default="images/company.png")
     
     def __str__(self):
          return self.c_name

class job_vacancy(models.Model):
     jv_id = models.AutoField(primary_key=True,unique=True)
     jv_name = models.CharField(max_length=50,default="")
     jv_category = models.CharField(max_length=50,default="")
     jv_time = models.CharField(max_length=50,default="")
     jv_location = models.CharField(max_length=50,default="")
     jv_city = models.CharField(max_length=50,default="")
     jv_pincode = models.CharField(max_length=50,default="")
     jv_salary = models.CharField(max_length=50,default="none")
     jv_exprince = models.CharField(max_length=50, default="fresher")
     jv_function = models.CharField(max_length=50,default="")
     jv_description = models.TextField(max_length=100000,default="")
     jv_key_responsibilites = models.TextField(max_length=100000,default="")
     jv_requirements = models.TextField(max_length=100000,default="")
     c_id = models.ForeignKey(Company,on_delete=models.CASCADE,to_field='c_id')
    

class apply_job(models.Model):
     aj_id = models.AutoField(primary_key=True)
     user_id = models.ForeignKey(User_t,on_delete=models.CASCADE,to_field='user_id')
     jv_id = models.ForeignKey(job_vacancy,on_delete=models.CASCADE,to_field='jv_id')
     c_id = models.ForeignKey(Company,on_delete=models.CASCADE,to_field='c_id')
     fname = models.CharField(max_length=50,default="")
     email = models.EmailField(max_length=50,default="")
     address = models.CharField(max_length=500,default="")
     city = models.CharField(max_length=50,default="")
     zip = models.CharField(max_length=50,default="")
     phone = models.CharField(max_length=50,default="")
     resume = models.FileField(upload_to='images/resume',default="")
     
class templates(models.Model):
     t_id = models.AutoField(primary_key=True)
     t_name = models.CharField(max_length=50)
     t_img = models.FileField(upload_to='t_img/',default="")     
     t_file = models.FileField(upload_to='templates_pdf/',blank=False)
     
     def __str__(self):
          return self.t_name
