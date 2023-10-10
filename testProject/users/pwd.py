from django.http import JsonResponse
import json
from common.models import Users
from django.contrib.auth.models import User

def changePwd(request):
    # 修改密码
    user = request.POST.get('user_name')
    old_pwd = request.POST.get('password_old')
    new_pwd = request.POST.get('password_new')

    usr = User.objects.get(username=user)
    if(usr.check_password(old_pwd)):
        usr.set_password(new_pwd)
        usr.save()
        return JsonResponse({
            'code': 200,
            'msg': '修改成功'
        })
    else:
        return JsonResponse({
            'code': 400,
            'msg': '旧密码错误'
        })
