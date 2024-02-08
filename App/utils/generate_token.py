import time
from datetime import datetime, timedelta
import jwt
from App.models import UserToken

# 生成token
def generate_token(username):
    # 设置过期时间为当前时间后的一小时
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    # 生成带有过期时间的JWT token
    secret_key = str(time.time())  # 用于签名的密钥
    token = jwt.encode({'username': username, 'exp': expiration_time}, secret_key, algorithm='HS256')

    # 检查是否存在该用户名的记录
    try:
        user_token = UserToken.objects.get(username=username)
        # 如果存在，更新记录
        user_token.token = token
        user_token.save()
    except UserToken.DoesNotExist:
        # 如果不存在，创建新记录
        user_token = UserToken.objects.create(username=username, token=token)
        user_token.save()

    return token
