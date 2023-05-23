from django.http import JsonResponse

def get_userInfo(request, id):
    if request.method == 'GET':
        usid = request.GET.get('usid','')
        if usid == '':
            return JsonResponse({'code': 0, 'msg':"用户id不能为空"})
        if usid == id:
            return JsonResponse({'code': 200, 'msg':"获取信息成功", 'data':{'name':"name", 'email':"email", 'gender':"gender", 'mobile':"mobile", 'nick_name':"123"}})
        else:
            return JsonResponse({'code': 404, 'msg':"记录不存在"})

def login(request, user_id, password, newpassword):
    if request.method == 'POST':
        if password == 'password':
            return JsonResponse({'code': 200, 'msg': '登录成功', 'data':{'access':"string"}})

def changePassword(request, password, newpassword):
    if request.method == 'POST':
        if password == 'password':
            password = newpassword
            return JsonResponse({'初始密码':password, '修改后密码':newpassword})

