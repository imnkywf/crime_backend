import json
import time
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

# 引入模型
from App.models import UserCredentials, UserProfile
from App.utils import generate_token
from App.models import UserAvatar


# 用户登录
class LoginView(View):

    def get(self, request):
        username = request.GET.get('username')  # 获取用户名
        password = request.GET.get('password')  # 获取密码

        print(username)
        print(password)

        # 检查是否有收到用户名和密码
        if not username or not password:
            return JsonResponse({'message': '登录失败，缺少用户名或密码'})

        try:
            check_user_credentials = UserCredentials.objects.get(username=username, password=password)
            check_user_credentials.save()

            # 如果找到了匹配的用户，则继续处理登录逻辑
            token = generate_token.generate_token(username)

            # 返回数据
            response_data = {
                'username': username,
                'password': password,
                'token': token,
            }
            return JsonResponse({'message': '登陆成功', 'data': response_data})
        except ObjectDoesNotExist:
            return JsonResponse({'message': '登录失败，用户名或密码错误'})


# 注册用户
class RegisterView(View):

    def post(self, request):
        json_data = json.loads(request.body.decode('utf-8'))

        username = json_data.get('username')  # 获取用户名
        password = json_data.get('password')  # 获取密码

        # 检查用户名是否已被注册
        if UserCredentials.objects.filter(username=username).exists():
            return JsonResponse({'message': '用户名已被注册'})

        # 生成token
        generate_token.generate_token(username)

        # 账号密码加进数据库
        add_user_credentials = UserCredentials(username=username, password=password)

        # 添加账号个人信息
        add_user_profile = UserProfile(username=username, gender='male', age=0, email='', address='',
                                       preferred_address='',
                                       create_time=time.time())

        # 添加头像
        add_user_avatar = UserAvatar(username=username, avatar_file_name='default.png')

        add_user_credentials.save()
        add_user_avatar.save()
        add_user_profile.save()
        response_data = {
            'username': username,
            'password': password,
        }

        return JsonResponse({'message': '注册成功', 'data': response_data})
