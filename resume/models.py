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
     u_img = models.ImageField(upload_to='images/user/',default="images/user.png")
     
     def __str__(self):
          return self.firstname

class Company(models.Model):
     c_id = models.AutoField(primary_key=True)
     c_name = models.CharField(max_length=50)
     c_email = models.OneToOneField(User,on_delete=models.CASCADE,to_field='username')
     c_password = models.CharField(max_length=50)
     c_location = models.CharField(max_length=50)
     c_img = models.ImageField(upload_to='images/compnay/',default="images/company.png")
     
     def __str__(self):
          return self.c_name

class job_vacancy(models.Model):
     jv_id = models.AutoField(primary_key=True)
     jv_name = models.CharField(max_length=50)
     jv_date = models.DateField()
     jv_description = models.TextField(max_length=500)
     jv_location = models.CharField(max_length=50)
     jv_no_of_vacancy = models.IntegerField(default=0)
     jv_eligibility = models.CharField(max_length=50)
     jv_exprince = models.CharField(max_length=50)
     c_id = models.ForeignKey(Company,on_delete=models.CASCADE,to_field='c_id')
    

class apply_job(models.Model):
     aj_id = models.AutoField(primary_key=True)
     a_date = models.DateField()
     user_id = models.ForeignKey(User_t,on_delete=models.CASCADE,to_field='user_id')
     jv_id = models.ForeignKey(job_vacancy,on_delete=models.CASCADE,to_field='jv_id')
     resume = models.FileField(upload_to='resume',default="")
     
class templates(models.Model):
     t_id = models.AutoField(primary_key=True)
     t_name = models.CharField(max_length=50)
     t_img = models.ImageField(upload_to='img',default=" ")
     t_file = models.FileField(upload_to='templates',default="")
     
     def __str__(self):
          return self.t_name
