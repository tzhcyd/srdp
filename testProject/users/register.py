from django.contrib.auth.models import User
from common.models import Users
from django.http import JsonResponse
from datetime import datetime

def register(request):
    # 注册
    if request.POST.get('email_code') == request.session['email_code']:
        email = request.POST.get('email')
        pwd = request.POST.get('password')

        user = User.objects.create_user(email, email, pwd)
        user.save()

        Users.objects.create(user_id=email,
                             email=email,
                             nick_name='未命名',
                             created_at=datetime.now()
                             )
        return JsonResponse({
            'code': 200,
            'msg': '注册成功'
        })
    else:
        return JsonResponse({
            'code': 400,
            'msg': '验证码错误'
        })

