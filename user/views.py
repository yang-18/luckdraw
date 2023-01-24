from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import re
import json
from utils.verify_data import validate_password, validate_email, validate_telephone, validate_name, get_effective_session
from utils.response_code import RET, error_map
from .models import UserModel
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserSerializers
import jwt
from luckdraw.settings import SECRET_KEY


# 注册
def Register(request):
    if request.method == "POST":
        telephone = request.GET.get('telephone')
        password = request.GET.get('password')
        username= request.GET.get('username')
        if validate_telephone(telephone):
            if validate_password(password):
                if UserModel.objects.filter(telephone=telephone).first():
                    return JsonResponse({'code': RET.USERERR, 'data': {'message': '该用户已存在'}})
                if UserModel.objects.filter(username=username).first():
                    return JsonResponse({'code': RET.USERERR, 'data': {'message': '该用户已存在'}})
                else:
                    user = UserModel()
                    user.telephone = telephone
                    user.password = make_password(password)
                    user.name = username
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    return JsonResponse({'code': 200, 'data': {'message': 'OK'}})
            else:
                return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '密码不能为空或太短'}})
        else:
            return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '手机号格式错误'}})



# # 登录方法
# def login(request):
#     if request.method == "POST":
#         json_str = request.body
#         json_dict = json.loads(json_str)
#         telephone = json_dict.get("telephone", None)
#         password = json_dict.get('password', None)
#         if telephone is None or password is None or len(telephone) == 0 or len(
#                 password) == 0:
#             return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '账号或密码不能为空。',
#                                                                 'token': 'None'}})
#         if not validate_telephone(telephone):
#             return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '手机号格式错误。',
#                                                                 'token': 'None'}})
#         if not validate_password(password):
#             return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '密码格式错误,密码应为3-18位英文字母或数字组成',
#                                                                 'token': 'None'}})
#         user = usermodel.objects.filter(telephone=telephone).first()
#         if user is None:
#             return JsonResponse({'code': RET.USERERR, 'data': {'message': '用户不存在，请先注册',
#                                                                'token': 'None'}})
#         user_data = UserSerializers(user).data
#         if password == user.password:
#             user.password = make_password(password)
#             user.save()
#         if (check_password(password, user.password)):
#             encoded_jwt = jwt.encode(
#                 {'telephone': telephone, 'password': password, 'id': user.id},
#                 SECRET_KEY, algorithm='HS256')
#             token = str(encoded_jwt)

#             # 查看用户是否是第一次登陆。如果是第一次，那就将Token存入数据库中
#             data = usermodel.objects.filter(token=token).first()
#             if data is None:
#                 user_token = usermodel()
#                 user_token.token = token
#                 user_token.user_id = user
#                 user_token.save()

#             # Logger.debug("用户登陆成功")
#             return JsonResponse({
#                 'code': 200,
#                 'data': {
#                     'message': '登录成功',
#                     'user_data': [user_data],
#                     'token': token
#                 }
#             })
#         else:
#             return JsonResponse({'code': RET.PWDERR,
#                                 'data': {'message': '密码错误，请重新输入密码',
#                                          'token': 'None'}})






