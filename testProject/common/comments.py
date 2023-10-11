from django.http import JsonResponse
import json
from common.models import Comments
from datetime import datetime
from django.http import HttpRequest

def getComments(request):
    taskid = request.GET.get('task_id',None)
    comments = Comments.objects.filter(task_id=taskid)

    comments_data = [] #用于存储评论的列表

    #遍历查询到的评论列表
    for comment in comments:
        comment_dict = {
            'user_id' : comment['user_id'],
            'body' : comment['body'],
            'picture' : comment['picture'],
            'created_at' : comment['created_at']
        }
        comments_data.append(comment_dict)

    #构建包含评论数据的响应字典
    response_Data = {
        'code' : 200,
        'msg' : '获取评论成功',
        'data' : comments_data
    }

    #返回JSON响应
    return JsonResponse(response_Data)

def createComment(request):
    info = request.GET.get('id',None)

    record = Comments.objects.create(task_id=info['task_id'],
                                     user_id=info['user_id'],
                                     body=info['body'],
                                     picture=info['picture'],
                                     created_at=datetime.now())
    return JsonResponse({
        'code' : 200,
        'msg' : '评论成功'
    })

def delectComment(request):
    commentid = request.GET.get('comment_id',None)
    userid = request.GET.get('userid',None)

    #判断是否为当前用户自己的评论
    session_data = request.session
    if 'user_id' in session_data:
        current_user_id = session_data['user_id']
        if current_user_id == userid:
            comment = Comments.objects.get(id=commentid)
            comment.delete()

            return JsonResponse({
                'code' : 200,
                'msg' : '评论删除成功'
            })
        else:
            return JsonResponse({
                'code' : 420,
                'msg' : '无法删除他人评论'
            })
    else:
        return JsonResponse({
            'code' : 400,
            'msg' : '请求有误'
        })

def likeComment(request):
    commentid = request.GET.get('comment_id',None)
    try:
        comment = Comments.objects.get(id=commentid)
    except Comments.DoesNotExist:
        return JsonResponse({
            'code' : 404,
            'msg' : '任务不存在'
        })

    comment.Like += 1
    comment.save()

    return JsonResponse({
        'code' : 200,
        'msg' : '点赞成功'
    })