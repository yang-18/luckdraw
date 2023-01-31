# from django.contrib import admin, messages
# from user.models import Surveyor, FeedBack, Stylist, Facility
# from .views import add_facility, add_Surveyor

# # Register your models here.


# # @admin.register(Surveyor)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'telephone', 'UserState',
#                     'add_time')   # 第一个参数可以是列表

#     # preview.allow_tags = True

#     # preview.short_description = "图片"

#     # 需要搜索的字段
#     search_fields = ('telephone', 'name')

#     # 右侧属性栏,可以
#     list_filter = ['telephone', 'name']

#     # 详情页可修改的字段
#     fields = ['name', 'telephone', 'password']

#     # 点击进入编辑的列
#     list_display_links = ['name', ]

#     # 分页显示，一页的数量
#     list_per_page = 5

#     actions_on_top = True
