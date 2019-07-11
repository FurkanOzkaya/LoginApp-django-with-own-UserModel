import re

def is_phone_number_valid(phone_number):
    """
    This function returns whether a given number is a valid phone number or not.

    All valid:

    International Numbers

    +905422672332

    1 800 5551212

    0543 555 1212

    5425551212

    18005551212

    +1800 555 1212 extension65432

    800 5551212 ext3333

    Invalids:

    234-911-5678

    :param phone_number:

    str

    An ip number

    :return result:

    boolean

    Whether the given phone number is valid or not
    """
    phone_number = str(phone_number)
    if(phone_number==""):
        return True
    else:
        international_pattern = re.compile(
        r'\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?')
    pattern = re.compile(
        r'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]‌​)\s*)|([2-9]1[02-9]|[2-9]['
        r'02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)([2-9]1[02-9]‌​|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?(['
        r'0-9]{4})\s*(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+)\s*)?$')
    result = False
    match1 = international_pattern.match(phone_number.lstrip('0'))
    match2 = pattern.match(phone_number.lstrip('0'))
    if match1 or match2:
        result = True
    return result

    


def is_email_valid(e_mail):
    """
    This function returns whether a given e mail address is valid or not.
    The regular expression is pretty simple but catches most of the valid email addresses. However, it does not have
    a wide sensitivity. Regex should be replaced with a more complex one for advanced usage.

    :param e_mail:

    str

    An e_mail address

    :return result:

    boolean

    Whether the given e_mail address is valid or not.
    """
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    result = False
    if pattern.match(e_mail):
        result = True
    return result

def is_password_valid(password):
    result = False
    password = str(password)
    if 50 >= len(password) >= 5:
        result = True
    return result

