import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import re
import json
from utils.verify_data import validate_password, validate_email, validate_telephone, validate_name, get_effective_session
from utils.response_code import RET, error_map
from utils.verify_token import verify_token, get_user_id
from .models import UserModel
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserSerializers
import jwt
from luckdraw.settings import SECRET_KEY
from django.core.mail import send_mail
# from utils.logging import Logger


# 注册
def register(request):
    if request.method == "POST":
        telephone = request.GET.get('telephone')
        password = request.GET.get('password')
        username = request.GET.get('username')

        if validate_telephone(telephone):
            if validate_password(password):
                if UserModel.objects.filter(telephone=telephone).first():
                    return JsonResponse({'code': RET.USERERR, 'data': {'message': '该用户已存在'}})
                elif UserModel.objects.filter(name=username).first():
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


# 登录方法
def login(request):
    if request.method == "POST":
        json_str = request.body
        json_dict = json.loads(json_str)
        telephone = json_dict.get("telephone")
        password = json_dict.get('password')
        # or len(telephone) == 0 or len(password) == 0
        if telephone is None or password is None:
            return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '账号或密码不能为空。',
                                                                'token': 'None'}})
        # if not validate_telephone(telephone):
        #     return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '手机号格式错误。',
        #                                                         'token': 'None'}})
        if not validate_password(password):
            return JsonResponse({'code': RET.PARAMERR, 'data': {'message': '密码格式错误,密码应为3-18位英文字母或数字组成',
                                                                'token': 'None'}})
        user = UserModel.objects.filter(telephone=telephone).first()
        if user is None:
            return JsonResponse({'code': RET.USERERR, 'data': {'message': '用户不存在，请先注册',
                                                               'token': 'None'}})
        user_data = UserSerializers(user).data
        # print(user_data)
        if password == user.password:
            # make_password(password, salt=None（指定时每次生成的密文相同）, hasher='default'（加密方法）)
            user.password = make_password(password)
            user.save()
        if (check_password(password, user.password)):    # check_password(明文，密文)  用于校验密码
            dic = {
                # 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),  # 设置到期时间
                'uid': user.id,
                'telephone': user.telephone,
                'password': user.password}
            encoded_jwt = jwt.encode(dic, SECRET_KEY, algorithm='HS256')
            token = str(encoded_jwt)
            # 查看用户是否是第一次登陆。如果是第一次，那就将Token存入数据库中
            token_data = UserModel.objects.filter(token=token).first()
            if token_data is None:
                UserModel.objects.create(token=token)
            return JsonResponse({
                'code': 200,
                'data': {
                    'message': '登录成功',
                    'user_data': [user_data],
                    'token': token
                }
            })
        else:
            return JsonResponse({'code': RET.PWDERR,
                                'data': {'message': '密码错误，请重新输入密码',
                                         'token': 'None'}})

# 个人中心


def personal_center(request):
    if request.method == "GET":
        # print(request)
        value = verify_token(request)
        print(value)
        if value is None:
            return JsonResponse({'code': RET.NOTOKEN, 'data': {'message': 'toekn令牌过期或错误'}})
        user_id = get_user_id(request=request)
        measuring = UserModel.objects.filter(id=user_id).first()
        if measuring is None:
            return JsonResponse({
                'code': 200,
                'data': {
                    'message': '用户不存在', }
            })

        serializers = UserSerializers(measuring)
        return JsonResponse({
            'code': 200,
            'data': {
                'message': '成功',
                'user_data': [serializers.data]}
        })


#  邮箱找回密码
def send_email(self, request):
    email = request.data.get('email')
    print(email)
    try:
        send_mail(subject="实验楼找回密码", message="点击链接修改密码", from_email="2754615732@qq.com",
                  recipient_list=[email],
                  html_message='请点击超链接<a href="http://127.0.0.1:8080/set_password?email={}">点击链接修改密码</a>'.format(email))
        return JsonResponse({'msg': '验证码已发送,请及时查收', 'code': 200}, status=200)
    except:
        return JsonResponse({'msg': '验证码发送失败'})


# 修改密码
def change_password(self, request):
    email = request.data.get('email')
    password = request.data.get('password')
    password2 = request.data.get('password2')

    if password == password2:
        UserModel.objects.filter(email=email).update(password=password)
        return JsonResponse({'msg': '密码修改成功', 'code': 200})
    else:
        return JsonResponse({'msg': '密码修改失败'}, status=502)
