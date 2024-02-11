import json

from django.http import JsonResponse
from django.views import View
from django.core.files.storage import default_storage

# 引入模型
from App.models import UserAvatar
import uuid


# 获取用户头像
class Avatar(View):

    def get(self, request):
        username = request.GET.get('username')
        print(username)

        avatar = UserAvatar.objects.get(username=username)

        return JsonResponse({'message': '获取成功', 'data': avatar.avatar_file_name})
        pass


# 上传用户头像
class Upload_Avatar(View):

    def post(self, request):
        # 从表单数据中获取 username
        username = request.POST.get('username', None)
        image_file = request.FILES.get('image')

        if username and image_file:
            # 使用 UUID 生成唯一文件名
            ext = image_file.name.split('.')[-1]  # 获取文件扩展名
            unique_filename = f"{uuid.uuid4()}.{ext}"  # 构建唯一文件名

            # 文件保存逻辑，使用 unique_filename 作为文件名
            file_path = default_storage.save(unique_filename, image_file)

            # 将文件信息保存到数据库
            # 这里假设每个用户只有一个头像，如果已存在则更新，否则创建
            UserAvatar.objects.update_or_create(
                username=username,
                defaults={'avatar_file_name': unique_filename}
            )

            return JsonResponse({'success': True, 'message': '上传成功', 'file_path': file_path})
        else:
            return JsonResponse({'success': False, 'message': '没有接收到文件或用户名'})
