from datetime import datetime

from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=20, blank = True, verbose_name = "姓名")
    email = models.EmailField(verbose_name="邮箱", null= True)
    nick_name = models.CharField(max_length=20, verbose_name="昵称",default="123")
    gender = models.CharField(max_length=6, default = "secret", verbose_name = "性别")
    mobile = models.CharField(max_length=20,verbose_name="手机号", null=True)
    avatar = models.ImageField(upload_to='img/%Y/%m/%d/',verbose_name="上传图片",null=True)
    created_at = models.DateTimeField(verbose_name="注册时间", default= datetime.now)

class participation(models.Model):
    user_id = models.IntegerField()
    task_id = models.IntegerField()
    is_accepted = models.BooleanField(verbose_name="是否接受邀请", default= False)
    created_at = models.DateTimeField(verbose_name="参与任务时间", default= datetime.now)

class tasks(models.Model):
    host_id = models.IntegerField()
    parent_id = models.IntegerField()
    title = models.CharField(max_length=20, verbose_name= "任务名称", default= "任务")
    body = models.TextField()
    plan_start_time = models.DateTimeField(verbose_name= "预计开始时间")
    plan_end_time = models.TimeField(verbose_name="预计结束时间")
    actual_start_time = models.TimeField(verbose_name="实际开始时间")
    actual_end_time = models.TimeField(verbose_name="实际结束时间")
    is_completed = models.BooleanField(verbose_name="是否完成任务", default= False)
    loop_mode = models.BooleanField(verbose_name="是否重复", default= False)
    created_at = models.DateTimeField(verbose_name="任务创建时间", default= datetime.now)

class friends(models.Model):
    user_id = models.IntegerField()
    friends_id = models.IntegerField()
    created_at = models.DateTimeField(default= datetime.now)

class comments(models.Model):
    task_id = models.IntegerField()
    user_id = models.IntegerField()
    body = models.TextField()
    picture = models.ImageField(upload_to='img/%Y/%m/%d/', verbose_name="上传图片", null= False)
    created_at = models.DateTimeField(verbose_name="评论发布时间", default=datetime.now)