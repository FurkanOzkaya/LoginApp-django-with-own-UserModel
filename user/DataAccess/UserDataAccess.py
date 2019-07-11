from ..models import User


def createUser(e_mail,password,first_name,last_name,phone_number):
    try:
        newUser=User(e_mail=e_mail,password=password,first_name=first_name,
                    last_name=last_name,phone_number=phone_number)
        newUser.save()
    except:
        newUser=None
        
    if newUser:
        return newUser

def get_user_replacate_by_email(e_mail):
    try:
        user = User.objects.get(e_mail=e_mail)
    except:
        user=None    
    if user:
        return True
    return False

def get_user_replacate_by_phone_number(phone_number):
    try:
        user = User.objects.get(phone_number=phone_number)
    except:
        user=None 
    if user:
        return True
    return False

def get_user_by_email(e_mail):
    try:
        user = User.objects.get(e_mail=e_mail)
    except:
        user=None
    return user



def get_user_by_id(id):
    try:
        user = User.objects.filter(id=id)
    except:
        user=None
    return user

def get_user_by_phone_number(phone_number):
    try:
        user = User.objects.get(phone_number=phone_number)
    except:
        user=None 
    return user

