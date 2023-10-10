from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import random

def random_str():
    _str = '1234567890'
    return ''.join(random.choice(_str) for i in range(5))

def send_email(request):
    if request.method == 'GET':
        try:
            email = request.GET['email']
        except:
            email = ''
        email_code = random_str()
        msg = '验证码：'+email_code
        send_mail('邮箱验证', msg, settings.EMAIL_FROM, [email])
        print(email_code)

        request.session['email_code'] = email_code
        return JsonResponse({
            'code': 200,
            'msg': '发送成功'
        })
    return JsonResponse({
        'code': 400,
        'msg': '错误'
    })