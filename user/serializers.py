from rest_framework import serializers
from .models import UserModel


class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    # # 头像
    # head_portrait = serializers.ImageField()
    # # 密码
    password = serializers.CharField(max_length=255)
    # 手机号
    telephone = serializers.CharField(max_length=11)
    # 昵称
    name = serializers.CharField(max_length=50)
  
    # 邮箱
    # email = serializers.CharField(max_length=255)

    class Meta:
        model = UserModel
        fields = ('id', 'telephone', 'name',
                   )
