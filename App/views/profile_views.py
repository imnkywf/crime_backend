import json

from django.db import IntegrityError
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

# 引入模型
from App.models import UserProfile


# 获取用户信息
class User_Profile(View):

    def get(self, request):
        try:
            username = request.GET.get('username')
            user_profile = UserProfile.objects.get(username=username)
            return JsonResponse({"message": "查询成功", "data": model_to_dict(user_profile)})

        except ObjectDoesNotExist:
            return JsonResponse({"message": "用户未找到", "data": {}})


# 更新用户信息
class Update_Profile(View):

    def post(self, request):
        json_data = json.loads(request.body.decode('utf-8'))  # 解析

        try:
            username = json_data.get('username')  # 获取用户名
            age = json_data.get('age')  # 获取年龄
            email = json_data.get('email')  # 获取邮箱
            address = json_data.get('address')  # 获取地址
            preferred_address = json_data.get('preferred_address')  # 获取偏好地址
            gender = json_data.get('gender')  # 获取性别

            user_profile = UserProfile.objects.get(username=username)


            user_profile.age = age
            user_profile.email = email
            user_profile.address = address
            user_profile.preferred_address = preferred_address
            user_profile.gender = gender

            user_profile.save()

            return JsonResponse({"message": "信息修改成功", "data": {}})

        except ObjectDoesNotExist:
            return JsonResponse({"message": "用户未找到", "data": {}})

        except IntegrityError:
            return JsonResponse({"message": "gender不能为null", "data": {}})
