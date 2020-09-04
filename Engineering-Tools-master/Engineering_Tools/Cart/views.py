from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from Company.models import Product_Hardware
from . models import Wishlist, Cart, Bookings, Order_No_For_User
import random
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
# Create your views here.

def Add_To_Wish_List_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id = P_ID)
        user = request.user
        Wishlist.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price, product_id=product.id, user_id=user.id)
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")


def Remove_From_Wish_List_View(request):
    if request.method == "POST":
        P_ID = request.POST.get("productId")
        Wishlist.objects.get(product= P_ID, user=request.user).delete()
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")



def Add_To_Wish_List_From_All_product_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        company_email = request.POST.get("CompanyEmail")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id = P_ID)
        user = request.user
        Wishlist.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price, product_id=product.id, user_id=user.id)
        return redirect(reverse('User:All_Product_By_Company', args=(company_email,)))
    else:
        return redirect("User:Home")


def Remove_From_Wish_List_From_All_Product_View(request):
    if request.method == "POST":
        company_email = request.POST.get("CompanyEmail")
        P_ID = request.POST.get("productId")
        Wishlist.objects.get(product= P_ID, user=request.user).delete()
        return redirect(reverse('User:All_Product_By_Company', args=(company_email,)))
    else:
        return redirect("User:Home")


def Remove_From_WishList_View(request):
    if request.method == "POST":
        ID = request.POST.get("ID")
        Wishlist.objects.get(id=ID, user=request.user).delete()
        return redirect('User:Wishlist')
    else:
        return redirect("User:Home")


def Add_To_Cart_From_Details_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id=P_ID)
        user = request.user
        Cart.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price,product_id=product.id, user_id=user.id, quantity=1, sub_total=price)
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")



def Remove_From_Cart_From_Details_View(request):
    if request.method == "POST":
        P_ID = request.POST.get("productId")
        Cart.objects.get(product= P_ID, user=request.user).delete()
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")


def Add_To_Cart_From_All_Product_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        company_email = request.POST.get("CompanyEmail")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id=P_ID)
        user = request.user
        Cart.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price,product_id=product.id, user_id=user.id, quantity=1, sub_total=price)
        messages.success(request, 'Your password has been changed successfully!')
        return redirect(reverse('User:All_Product_By_Company', args=(company_email,)))
    else:
        return redirect("User:Home")

def Remove_From_Cart_From_All_Product_View(request):
    if request.method == "POST":
        P_ID = request.POST.get("productId")
        company_email = request.POST.get("CompanyEmail")
        Cart.objects.get(product= P_ID, user=request.user).delete()
        return redirect(reverse('User:All_Product_By_Company', args=(company_email,)))
    else:
        return redirect("User:Home")

def Wishlist_To_cart_View(request):
    if request.method == "POST":
        id = request.POST.get('ID')
        data = Wishlist.objects.get(id = id)
        Cart.objects.create(product_name=data.product_name, user_name=data.user_name, user_email=data.user_email, price=data.price,
                            product_id=data.product_id, user_id=data.user_id, quantity=1, sub_total=data.price)
        Wishlist.objects.filter(id=id).delete()
        return redirect('User:Wishlist')
    else:
        return redirect('User:Wishlist')

def Remove_Product_From_Cart_View(request):
    if request.method == "POST":
        CartID = request.POST.get("CartID")
        Cart.objects.get(id=CartID).delete()
        return redirect("User:Cart")

def Remove_All_Product_View(request):
    if request.method == "POST":
        UserID = request.user.id
        Cart.objects.filter(user=UserID).delete()
        return redirect("User:Cart")


def Checkout_View(request):
    if request.method == "POST":
        user_id = request.user.id
        dataFromCart = Cart.objects.filter(user=user_id)
        TOTAL = 0
        for i in range(0, len(dataFromCart)):
            TOTAL = TOTAL + float(dataFromCart[i].sub_total)
        ORDER = str(random.randint(100000,999999))
        Order_No_For_User.objects.create(order_no=ORDER,total_price= TOTAL)
        ORDER_NO = Order_No_For_User.objects.get(order_no = ORDER)
        for i in range(0,len(dataFromCart)):
            Bookings.objects.create(user_name=request.user.username,user_email=request.user.email,product_name=dataFromCart[i].product_name,price=dataFromCart[i].price,order_no_id=ORDER_NO.id,user=request.user)
        Cart.objects.filter(user_id = request.user.id).delete()

        # email ORDER send Logic
        subject = "Order No: " + ORDER + " Invoice From Engineering Tools"
        message ="Your Order Is Booked And Your Total Price is : " + str(TOTAL) + "$."
        email_from = settings.EMAIL_HOST_USER
        email_to = [request.user.email, ]
        send_mail(subject, message, email_from, email_to)
        # email ORDER done
        return redirect('User:Cart')
    else:
        return redirect('User:Cart')