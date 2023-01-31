from django.contrib import admin, messages
from games.models import ProductModel
# from .views import add_facility, add_Surveyor
# Register your models here.


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'act_amount',
                    'sal_amount', 'total_sales', 'stock', 'source', 'type')

    # 分页显示，一页的数量
    list_per_page = 5
