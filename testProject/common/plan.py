from django.http import JsonResponse
import json
from common.models import Tasks
from datetime import datetime

def createTask(request):
    info = request.params['data']
    #从消息请求中获取要添加任务的信息
    #插入到数据库中
    record = Tasks.objects.create(plan_end_time=info['plan_end_time'],
                                  plan_start_time=info['plan_start_time'],
                                  body=info['body'],
                                  title=info['title'],
                                  loop_mode=info['loop_mode'],
                                  created_at=datetime.now())

    return JsonResponse({
        'code' : 200,
        'msg' : '添加任务成功'
    })

def changeTask(request):
    taskid = request.params['id']
    newdata = request.params['data']

    try:
        task = Tasks.objects.get(task_id=taskid)
    except Tasks.DoesNotExist:
        return JsonResponse({
            'code' : 404,
            'msg' : '任务不存在'
        })

    if 'title' in newdata:
        task.title = newdata['title']
    if 'body' in newdata:
        task.body = newdata['body']
    if 'plan_start_time' in newdata:
        task.plan_start_time = newdata['plan_start_time']
    if 'plan_end_time' in newdata:
        task.plan_end_time = newdata['plan_end_time']
    if 'actual_start_time' in newdata:
        task.actual_start_time = newdata['actual_start_time']
    if 'actual_end_time' in newdata:
        task.actual_end_time = newdata['actual_end_time']
    if 'loop_mode' in newdata:
        task.loop_mode = newdata['loop_mode']
    task.save()

    return JsonResponse({
        'code' : 200,
        'msg' : '任务修改成功'
    })

def endPlan(request):
    taskid = request.params['task_id']
    text = request.params['text']

    try:
        task = Tasks.objects.get(task_id=taskid)
    except Tasks.DoesNotExist:
        return JsonResponse({
            'code' : 404,
            'msg' : '任务不存在'
        })
    task.is_completed = True
    task.text = text

    task.save()

    return JsonResponse({
        'code' : 200,
        'msg' : '结束任务成功'
    })

def delect(request):
    taskid = request.params['task_id']
    task = Tasks.objects.get(task_id=taskid)
    task.delete()

    return JsonResponse({
        'code' : 200,
        'msg' : '删除任务成功'
    })