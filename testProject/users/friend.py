from django.http import JsonResponse
from common.models import Friend
from common.models import Users
from datetime import datetime

def addfriend(request):
    if request.user.is_authenticated:
        userid = request.POST.get('user_id')
        friendid = request.POST.get('friend_id')

        users = Users.objects.values()
        user = users.filter(user_id=userid)
        if user:
            Friend.objects.create(user_id=userid, friend_id=friendid, created_at=datetime.now())
            return JsonResponse({
                'code': 200,
                'msg': '请求发送成功'
            })
        else:
            return JsonResponse({
                'code': 400,
                'msg': '用户不存在'
            })

    else:
        return JsonResponse({
            'code': 401,
            'msg': '未登录'
        })

def delfriend(request):
    if request.user.is_authenticated:
        userid = request.POST.get('user_id')
        friendid = request.POSYT.get('friend_id')

        users = Users.objects.values()
        user = users.filter(user_id=friendid)
        if user:
            obj = Friend.objects.get(user_id=userid, friend_id=friendid)
            obj.delete()
            obj = Friend.objects.get(user_id=friendid, friend_id=userid)
            obj.delete()
            return JsonResponse({
                'code': 200,
                'msg': '删除成功'
            })
        else:
            return JsonResponse({
                'code': 400,
                'msg': '用户不存在'
            })

    else:
        return JsonResponse({
            'code': 401,
            'msg': '未登录'
        })

def getlist(request):
    if request.user.is_authenticated:
        userid = request.POST.get('user_id')
        friends = Friend.objects.values()
        friend = friends.filter(user_id=userid)

        user_data = []
        for user in friend:
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

        response_data = {
            'code': 200,
            'msg': '获取成功',
            'data': user_data
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({
            'code': 401,
            'msg': '未登录'
        })

def denyfriend(request):
    if request.user.is_authenticated:
        userid = request.POST.get('user_id')
        friendid = request.POSYT.get('friend_id')

        users = Users.objects.values()
        user = users.filter(user_id=friendid)
        if user:
            obj = Friend.objects.get(user_id=friendid, friend_id=userid)
            obj.delete()
            return JsonResponse({
                'code': 200,
                'msg': '拒绝成功'
            })
        else:
            return JsonResponse({
                'code': 400,
                'msg': '用户不存在'
            })

    else:
        return JsonResponse({
            'code': 401,
            'msg': '未登录'
        })