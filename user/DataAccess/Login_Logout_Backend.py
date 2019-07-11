from ..models import User
from .UserDataAccess import get_user_by_email
from django.shortcuts import redirect
#from django.contrib.sessions import *


def login_process(request=None,e_mail=None,password=None):
    user=get_user_by_email(e_mail=e_mail)
    if user.password==password:
        if user.is_active==True:
            user.save()
            request.session.__setitem__("id",user.id)
            request.session.__setitem__("password",user.password)
            request.session.__setitem__("e_mail",user.e_mail)
            request.session.set_expiry(300)          
    return user

def login_requried(request):
        id = request.session.get("id",0)
        if id != 0:
                return True
        return False
        