from django.contrib import admin

# Register your models here.

from .models import Product, Category, Company, ProductSize, ProductSite, Comment
from django.contrib.auth.models import Group

#To see our models on the admin panel. We need to register these models on the Django Admin.
#We see the models even when empty.

#For advanced model configuration we must use ModelAdmin Class. The ModelAdmin class is a representation of user-defined models in the admin panel. It can be used to override various actions. First we need to create and register ModelAdmin Class. We can use @admin.register decorator or admin.site.register() method for registiration. We can use @register decorator.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #list_display = ('pk', 'name', 'content')
    list_display = ('pk', 'name')
    list_filter = ('category', )

#admin.site.register(Product, ProductAdmin) <- admin.site.register method

#admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)

#If we want to remove default models like Groups from admin, we can use unregister method.
admin.site.unregister(Group)

# To change site written in thr top-left corner of the web
admin.site.site_header = "Product Review Admin"