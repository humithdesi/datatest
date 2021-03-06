from django.contrib import admin

from .Models.M_Product import BoSuuTap,ThuongHieu,LoaiGa,LoaiNem,ChatLieu,KichThuoc,DoDay,Product,Review,LikeProduct
from .Models.M_Order import Order
from .Models.M_TinTuc import TinTuc
# Register your models here.
class TagAdminOrder(admin.ModelAdmin):
    list_display = ['phone', 'product','quantity','date']
    list_filter = ['phone','date','product','address']
    search_fields = ['phone','product','address']


admin.site.register(Order,TagAdminOrder)



class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'thuongHieu']
    list_filter = ['thuongHieu','chatLieu','boSuuTap','loaiGa','loaiNem']
    search_fields = ['thuongHieu','chatLieu','boSuuTap','loaiGa','loaiNem']
    prepopulated_fields = {'slug': ('name',)}

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
class TagReview(admin.ModelAdmin):
    list_display = ['product','comment','date']
    list_filter = ['user','date','product']
    search_fields = ['user','date','product']

from django_summernote.admin import SummernoteModelAdmin
class TinTucAdmin(SummernoteModelAdmin):
    # displaying posts with title slug and created time
    list_display = ('title', 'slug',)
    list_filter = ("title",)
    search_fields = ['title', 'content']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('content', )

admin.site.register(BoSuuTap,SlugAdmin)
admin.site.register(ThuongHieu,SlugAdmin)
admin.site.register(LoaiGa,SlugAdmin)
admin.site.register(LoaiNem,SlugAdmin)
admin.site.register(ChatLieu,SlugAdmin)
admin.site.register(KichThuoc,SlugAdmin)
admin.site.register(DoDay,SlugAdmin)
admin.site.register(Product,TagAdmin)
admin.site.register(Review,TagReview)
admin.site.register(TinTuc,TinTucAdmin)
admin.site.register(LikeProduct)