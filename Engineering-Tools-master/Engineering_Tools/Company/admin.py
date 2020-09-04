from django.contrib import admin
from .models import Register, Company_Profile, Product_Catagory, Product_Hardware, Product_software, Product_Review

# Register your models here.
admin.site.register(Register)
admin.site.register(Company_Profile)
admin.site.register(Product_Catagory)
admin.site.register(Product_Hardware)
admin.site.register(Product_software)
admin.site.register(Product_Review)