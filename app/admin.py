from django.contrib import admin
from .models import Banner,Category,Brand,Size,Color,Product,ProductAttribute
# Register your models here.

admin.site.register(Brand)
admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_bg')
admin.site.register(Color,ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','brand','is_featured','status')
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','product','price','color','size')
admin.site.register(ProductAttribute ,ProductAttributeAdmin )