import json
import logging

from django.http import JsonResponse
from django.shortcuts import render



logger = logging.getLogger('log')


def index(request, _):
    """
    获取主页

     `` request `` 请求对象
    """

    return render(request, 'index.html')

def login(request, _):
    """
    登录

    `` request `` 请求对象
    """

    return render(request, 'login.html')
