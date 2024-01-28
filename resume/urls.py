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
    path('u_admin/',views.u_admin,name='u_admin'),
    path('table/',views.table,name='table'),
]