import jwt
from luckdraw.settings import SECRET_KEY
from user.models import UserModel
import json


# 验证token是否存在
def verify_token(request):
    # token = request.GET.get('token')
    # print(token)
    try:
        json_str = request.body
        if len(json_str) > 0:
            json_dict = json.loads(json_str)   # json.loads()  这个函数是将json格式数据转换为字典
            token = json_dict['token']
            print(token)
        else:
            token = request.GET.get('token')
            # print(token)
        token = request.GET.get('token')
        print(token)
        data = UserModel.objects.filter(token=token).first()
        if data:
            return data
        else:
            return None
    except AttributeError:
        return None


def get_user_id(request):
    try:
        json_str = request.body
        if len(json_str) > 0:
            json_dict = json.loads(json_str)
            token = json_dict['token']
        else:
            token = request.GET.get('token')
        # 解析token字段
        decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except AttributeError:
        return None
    return decode_jwt['id']


# def check_measure_id(request, measure_task):
#     # 检查这个任务是否属于这个用户
#     # 提出token中的用户id，然后用测量任务的user_id进行对比
#     if get_user_id(request) == measure_task.Sid.id:
#         return True
#     else:
#         return False
