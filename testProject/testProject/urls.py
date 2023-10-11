"""testProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users.user_info import dispatcher
from users import log_in_out
from users.register import register
from users.email_send import send_email
from users import friend
from common.views import mytest

urlpatterns = [
    path('', mytest),
    path('admin/', admin.site.urls),
    path('user/reg', register),
    path('user/login', log_in_out.signin),
    path('user/logout', log_in_out.signout),
    path('email/login', log_in_out.emailsignin),
    path('user/info', dispatcher),
    path('email/send', send_email),
    path('user/friend/add', friend.addfriend),
    path('user/friend/delete', friend.delfriend),
    path('user/friend/list', friend.getlist),
    path('user/friend/deny', friend.denyfriend),
    path('task/',include('common.urls'))
]
