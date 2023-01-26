import re
from django.contrib.sessions.models import Session
import datetime
import pytz


def validate_telephone(tel):
    # print(tel)
    if tel is not None:
        telephone = re.match(r"^1[35678]\d{9}$", tel)
        if telephone: 
            print(telephone)
            return True
        else:
            False
    else:
        return False


def validate_name(name):
    if name is not None and len(name) > 0:
        return True
    else:
        return False


def validate_email(email):
    if email is not None:
        if re.match(
                "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
        else:
            return False
    else:
        return False


def validate_password(pwd):
    if pwd is not None:
        if re.match("\d\S{3,16}$", pwd):
            return True
        else:
            return False
    else:
        return False

# 获取有效的sessing


def get_effective_session():
    session_list = []
    obj = Session.objects.filter()
    date = datetime.datetime.now().replace(tzinfo=pytz.timezone('UTC'))
    for data in obj:
        if data.expire_date > date:
            session_list.append(data)
    return session_list
