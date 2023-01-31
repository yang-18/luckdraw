from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="更改时间")

    # 不生成表，默认会自动生成一个表
    class Meta:
        abstract = True


# 产品表(product)
class ProductModel(BaseModel, models.Model):

    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="产品名称")
    number = models.CharField(max_length=255, verbose_name="产品编号")
    act_amount = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="实际金额")
    sal_amount = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="销售金额")
    total_sales = models.IntegerField(default=0, verbose_name="总销售数量")
    stock = models.IntegerField(default=0, verbose_name="库存")
    source = models.IntegerField(
        default=0, verbose_name="来源渠道")  # 0：淘宝   1：    2：
    type = models.IntegerField(
        default=0, verbose_name="产品类型")  # 0：游戏   1：贴纸  2：现金

    # 创建表名
    class Meta():
        verbose_name_plural = "产品表"
        db_table = 'product'

    # 直接显示name,不加显示的是object对象
    def __str__(self):
        return self.name
