# Add this to your tasks.py or create a new file for tasks
from collections import UserDict
from celery import shared_task
from django.contrib.auth import logout
from django.utils import timezone
from django.contrib.sessions.models import Session
from requests import request
from django.utils import timezone
@shared_task
def check_user_activity():
    # Set the inactivity timeout to 1 hour (3600 seconds)
    inactivity_timeout = 3600
    cutoff_time = timezone.now() - timezone.timedelta(seconds=inactivity_timeout)
    
    # Get active sessions and log out users who have been inactive for more than 1 hour
    for session in Session.objects.filter(expire_date__gte=timezone.now()):
        session_data = session.get_decoded()
        user_id = session_data.get('_auth_user_id')
        if user_id:
            user_last_activity = timezone.make_aware(session_data['last_activity'])
            if user_last_activity < cutoff_time:
                logout_user(user_id)

def logout_user(user_id):
    user = UserDict.objects.get(pk=user_id)
    logout(request)
    # Optionally, you can perform additional cleanup or logging before logging the user out
    # For example: user.last_activity = None; user.save()
