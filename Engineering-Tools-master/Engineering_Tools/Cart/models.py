from django.db import models
from Company.models import Product_Hardware
from django.contrib.auth.models import User
# Create your models here.

class Wishlist(models.Model):
    product = models.ForeignKey(Product_Hardware, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 20)
    user_name = models.CharField(max_length = 20)
    user_email = models.EmailField()
    price = models.CharField(max_length=10)
    added_in_wishlist = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name + " / " + self.user_name

class Cart(models.Model):
    product = models.ForeignKey(Product_Hardware, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 20)
    user_name = models.CharField(max_length = 20)
    user_email = models.EmailField()
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length = 2)
    sub_total = models.CharField(max_length=30)
    added_in_cart = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name + " / " + self.user_name

class Order_No_For_User(models.Model):
    order_no = models.CharField(max_length = 6)
    total_price = models.CharField(max_length = 10)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_no

class Bookings(models.Model):
    order_no = models.ForeignKey(Order_No_For_User, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_name = models.CharField(max_length = 25)
    user_email = models.EmailField()
    product_name = models.CharField(max_length = 20)
    price = models.CharField(max_length = 8)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name + " / " + str(self.order_no)
