# Task_1
import re
RE_VALID = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$')


def email_parse(user_email):
        if RE_VALID.match(user_email):
            user_domain = str((re.split(r'^[a-z0-9._%+-]+@',user_email))[1])
            user_name = str((re.split(r'@[a-z0-9.-]+\.[a-z]{2,}$',user_email))[0])
            print({'username': user_name, 'domain': user_domain})
        else:
            print(f'email address {user_email} invalid')