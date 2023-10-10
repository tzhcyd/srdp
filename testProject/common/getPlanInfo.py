from django.http import JsonResponse
import json
from common.models import Tasks


def getTaskInfo(request):
    task = Tasks.objects.values()
    task_id = request.GET.get('task_id',None)

    #如果提供了task_id参数，只查询特定任务信息
    if task_id:
        tasks = task.filter(task_id=task_id)

    task_data = [] #用于存储任务数据的列表

    #遍历查询到的任务信息
    for task in tasks:
        task_dict = {
            'task_id' : task['task_id'],
            'title' : task['title'],
            'body' : task['body'],
            'plan_start_time' : task['plan_start_time'],
            'plan_end_time' : task['plan_end_time'],
            'actual_start_time' : task['actual_start_time'],
            'actual_end_time' : task['actual_end_time'],
            'loop_mode' : task['loop_mode'],
            'status' : task['is_completed'],
            'create_at' : task['create_at']
        }
        task_data.append(task_dict)

    #构建包含任务数据的响应字典
    response_data = {
        'code' : 200,
        'msg' : '获取成功',
        'data' : task_data
    }

    #返回JSON响应
    return JsonResponse(response_data)

def getTaskInfoInDate(request):
    date = request.GET.get('date',None)
    tasks = Tasks.objects.filter(created_at=date)

    task_data = []  # 用于存储任务数据的列表

    # 遍历查询到的任务信息
    for task in tasks:
        task_dict = {
            'task_id': task['task_id'],
            'title': task['title'],
            'body': task['body'],
            'plan_start_time': task['plan_start_time'],
            'plan_end_time': task['plan_end_time'],
            'actual_start_time': task['actual_start_time'],
            'actual_end_time': task['actual_end_time'],
            'loop_mode': task['loop_mode'],
            'status': task['is_completed'],
            'create_at': task['create_at']
        }
        task_data.append(task_dict)

    #构建包含任务数据的响应字典
    response_data = {
        'code' : 200,
        'msg' : '获取成功',
        'data' : task_data
    }
    return JsonResponse(response_data)

def getHistroyTaskInfo(request):
    tasks = Tasks.objects.filter(host_id=request.GET.get('host_id',None))

    task_data = []  # 用于存储任务数据的列表

    # 遍历查询到的任务信息
    for task in tasks:
        task_dict = {
            'task_id': task['task_id'],
            'title': task['title'],
            'body': task['body'],
            'plan_start_time': task['plan_start_time'],
            'plan_end_time': task['plan_end_time'],
            'actual_start_time': task['actual_start_time'],
            'actual_end_time': task['actual_end_time'],
            'loop_mode': task['loop_mode'],
            'status': task['is_completed'],
            'create_at': task['create_at']
        }
        task_data.append(task_dict)

    #构建包含任务数据的响应字典
    response_data = {
        'code' : 200,
        'msg' : '获取成功',
        'data' : task_data
    }
    return JsonResponse(response_data)