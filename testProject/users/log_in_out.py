from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

def signin(request):
    # 登录
    userid = request.POST.get('user_id')
    pwd = request.POST.get('password')

    user = authenticate(user_id=userid, password=pwd)

    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({
                'code': 200,
                "msg": '成功'
            })
        else:
            return JsonResponse({
                'code': 500,
                "msg": '意外错误'
            })
    else:
        return JsonResponse({
            'code': 420,
            'msg': '用户名或密码错误'
        })

def emailsignin(request):
    # 邮箱登录
    email = request.POST.get('email')
    email_code = request.POST.get('email_code')

    user = authenticate(email=email)

    if user is not None:
        if request.session['email_code'] == email_code:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = email
                return JsonResponse({
                    'code': 200,
                    'msg': '成功'
                })
            else:
                return JsonResponse({
                    'code': 500,
                    'msg': '意外错误'
                })
        else:
            return JsonResponse({
                'code': 400,
                'msg': '验证码错误'
            })
    else:
        return JsonResponse({
            'code': 420,
            'msg': '用户名或密码错误'
        })

def signout(request):
    # 退出登录
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({
            'code': 200,
            'msg': '成功'
        })
    else:
        return JsonResponse({
            'code': 400,
            'msg': '未登录'
        })
