from django.contrib import admin
from django.urls import path

from . import plan, getPlanInfo
from .getPlanInfo import *
from .plan import *

urlpatterns = [
    path('new/', plan.createTask),
    path('', getTaskInfo),
    path('day/',getTaskInfoInDate),
    path('history/',getHistroyTaskInfo),
    path('edit/',changeTask),
    path('complete/',endPlan)
]
