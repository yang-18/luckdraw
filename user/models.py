from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="更改时间")

    # 不生成表，默认会自动生成一个表
    class Meta:
        abstract = True


# 用户(user)
class UserModel(BaseModel, models.Model):
    # id  主键
    id = models.AutoField(primary_key=True, verbose_name="ID")

    name = models.CharField(max_length=50, unique=True,
                            verbose_name="昵称")

    head_portrait = models.ImageField(
        upload_to='img', null=True, verbose_name="头像")
    password = models.CharField(max_length=255, verbose_name="密码")
    telephone = models.CharField(
        max_length=22, unique=True, verbose_name="手机号码")

    email = models.CharField(max_length=255, null=True, unique=True,
                             verbose_name="邮箱")
    level = models.IntegerField(null=True, default=1, verbose_name="等级")
    balance = models.DecimalField(
        null=True, max_digits=5, decimal_places=2, verbose_name="余额")
    consumption = models.DecimalField(
        null=True, max_digits=5, decimal_places=2, verbose_name="消费")
    recharge = models.DecimalField(
        null=True, max_digits=5, decimal_places=2, verbose_name="充值")
    token = models.CharField(max_length=300, null=True,
                             unique=True, verbose_name="token")

    # 创建表名
    class Meta():
        verbose_name_plural = "用户"
        db_table = 'usermodel'

    # 直接显示name,不加显示的是object对象
    def __str__(self):
        return self.name


# 管理员(admintable)
class AdmintableModel(AbstractUser, BaseModel,):
    # id 主键
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="昵称")
    password = models.CharField(max_length=255, verbose_name="密码")
    telephone = models.CharField(
        max_length=22, unique=True, verbose_name="手机号码")
    email = models.CharField(max_length=255, null=True, unique=True,
                             verbose_name="邮箱")
    level = models.IntegerField(null=True, default=1, verbose_name="等级")

    # 创建表名
    class Meta():
        verbose_name_plural = "管理员"
        db_table = 'admintable'

    # 直接显示name,不加显示的是object对象
    def __str__(self):
        return self.name


# # 订单表（）
# # id：  支付方式：  付款备注：  当前状态：  消费时间
# # 订单编号：  消费金额： 收单机构(Acquirer)  订单状态：  外键（产品）：
# # 外键（用户）：

# # 订单表(order)
# class OrderModel(BaseModel, models.Model):
#     # 主键 id
#     id = models.AutoField(primary_key=True, verbose_name="ID")
#     payment = models.IntegerField(default=0,verbose_name="支付方式")  #  0：支付宝   1：微信    2：
#     pay_remarks = models.CharField(max_length=255, verbose_name="付款备注")
#     state = models.IntegerField(default=0,verbose_name="支付状态")  #  0：未支付   1：已支付
#     payment_time = models.DateTimeField(verbose_name="支付时间")    # auto_now   每次执行 save 操作时，将其值设置为当前时间，并且每次修改model，都会自动更新
#     order_id = models.IntegerField(max_length=255, verbose_name="订单编号")
#     con_amount = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="消费金额")
#     Acquirer =models.CharField(max_length=50, null=True,verbose_name="收单机构")

#     # user_id(用户外键)
#     # product_id(商品外键)

#     # 创建表名
#     class Meta():
#         verbose_name_plural = "订单表"
#         db_table = 'order'

#     # 直接显示name,不加显示的是object对象
#     def __str__(self):
#         return self.name
