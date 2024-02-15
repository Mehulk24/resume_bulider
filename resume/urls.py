from django.contrib import admin
from django.urls import path,include
from resume import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.hlogin,name='login'),
    path('sing_up/',views.sing_up,name='sing_up'),
    path('email/',views.email,name='email'),
    path('company/',views.company,name='company'),
    path('company_login/',views.company_login,name='company_login'),
    path('c_email/',views.c_email,name='c_email'),
    path('profile/',views.profile,name='profile'),
    path('template/',views.template,name='template'),
    path('job/',views.job,name='job'),
    path('logout/',views.my_logout,name='logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),   
    path('c_home/',views.c_home,name='c_home'),
    path('u_admin/',views.admin_login,name='u_admin'),
    path('table/',views.table,name='table'),
    path('upload/',views.upload_templates,name='upload'),
    path('a_dasbord/',views.a_dasbord,name='a_dasbord'),
    path('job_details/<int:jv_id>/',views.job_details,name='job_details'),
    path('u_deletes/<int:user_id>/',views.u_deletes,name='u_deletes'),
    path('c_deletes/<int:c_id>/',views.c_deletes,name='c_deletes'),
    path('j_deletes/<int:jv_id>/',views.j_deletes,name='j_deletes'),
    path('t_deletes/<int:t_id>/',views.t_deletes,name='t_deletes'),
    path('post_job',views.post_job,name='post_job'),
    
]