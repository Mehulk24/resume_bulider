from django.contrib import admin
from resume.models import User_t,compnay,job_vacancy,apply_job,templates

# Register your models here.

admin.site.register(User_t)
admin.site.register(compnay)
admin.site.register(job_vacancy)
admin.site.register(apply_job)
admin.site.register(templates)

