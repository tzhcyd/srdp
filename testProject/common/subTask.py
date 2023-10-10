from django.http import JsonResponse
import json
from common.models import Tasks
from datetime import datetime

def createSubTask(request):
    info = request.params['data']

    record = Tasks.objects.create(
        parent_id=info['parent_id'],
        plan_end_time=info['plan_end_time'],
        plan_start_time=info['plan_start_time'],
        body=info['body'],
        title=info['title'],
        loop_mode=info['loop_mode'],
        created_at=datetime.now())

    return JsonResponse({
        'code' : 200,
        'msg' : '任务添加成功'
    })

def deleteSubTask(request):
    taskid = request.params['task_id']
    task = Tasks.objects.get(task_id=taskid)
    task.delete()

    return JsonResponse({
        'code' : 200,
        'msg' : '任务删除成功'
    })