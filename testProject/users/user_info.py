from django.http import JsonResponse
import json
from common.models import Users

def dispatcher(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'code': 400,
            'msg': '未登录',
        })
    if request.method == 'GET':
        request.params = request.GET
        return getuserinfo(request)
    elif request.method == 'POST':
        request.params = json.loads(request.body)
        return changeuserinfo(request)
    else:
        return JsonResponse('ERROR')


def getuserinfo(request):
    # 获取用户信息
    users = Users.objects.values()

    user_id = request.GET.get('user_id', None)

    # 如果提供了user_id参数，只查询特定用户信息
    if user_id:
        users = users.filter(id=user_id)

    user_data = []  # 用于存储用户数据的列表

    # 遍历查询到的用户信息
    for user in users:
        user_dict = {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'gender': user['gender'],
            'mobile': user['mobile'],
            'nick_name': user['nick_name'],
            'avatar': user['avatar']
        }
        user_data.append(user_dict)

    # 构建包含用户数据的响应字典
    response_data = {
        'code': 200,
        'msg': '获取成功',
        'data': user_data
    }

    # 返回JSON响应
    return JsonResponse(response_data)

def changeuserinfo(request):
    # 修改用户信息
    userid = request.params['id']
    info = request.params['data']

    try:
        user = Users.objects.get(user_id=info['user_id'])
    except Users.DoesNotExist:
        # record = Users.objects.create(user_id=info['user_id'], nick_name=info['nick_name'], avatar=info['avatar'],
        # email=info['email'], mobile=info['mobile'], gender=info['gender'], name=info['name'])
        return JsonResponse({
            'code': 400,
            'msg': '找不到用户'
        })
    if 'name' in info:
        user.name = info['name']
    if 'email' in info:
        user.email = info['email']
    if 'nick_name' in info:
        user.nick_name = info['nick_name']
    if 'gender' in info:
        user.gender = info['gender']
    if 'mobile' in info:
        user.mobile = info['mobile']
    if 'avatar' in info:
        user.avatar = info['avatar']
    user.save()

    return JsonResponse({
        'code': 200,
        'msg': '成功'
    })
