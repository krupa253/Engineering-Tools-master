from django.contrib import admin
from .models import Wishlist, Cart, Order_No_For_User, Bookings
# Register your models here.

admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order_No_For_User)
admin.site.register(Bookings)
