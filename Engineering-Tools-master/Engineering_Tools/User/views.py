from django.shortcuts import render, redirect, reverse
from .models import Profile
from Company.models import Company_Profile, Product_Hardware, Register, Product_Catagory, Product_Review
from Company.forms import Product_Review_form
from Cart.models import Wishlist, Cart, Bookings, Order_No_For_User
# Create your views here.

def Home_View_User(request):
    temp = "User/index.html"
    return render(request, temp)

def My_Account_View(request):
    temp = "User/my_account.html"
    ID = request.user.id
    data = Profile.objects.get(user_id = ID)
    print(data.gender)
    return render(request, temp, {'data':data})


def Update_Account_Info_View(request):
    if request.method == 'POST':
        number = request.POST.get("PhoneNumber")
        Gender = request.POST.get("genderSelect")
        Address = request.POST.get("address")
        City = request.POST.get("city")
        State = request.POST.get("state")
        Country = request.POST.get("country")
        Pincode = request.POST.get("pincode")
        ID = request.user.id
        Profile.objects.filter(user_id=ID).update(phone=number, gender=Gender, address_line=Address, city=City, state=State, country=Country, pincode=Pincode)
        return redirect('User:Home')
    else:
        return redirect('User:My_Account')


def All_Company_View(request):
    temp = "User/all_company.html"
    data = Company_Profile.objects.all()
    return render(request, temp, {'data':data})

def All_Product_By_Company(request, email):
    temp = "User/all_product_by_company.html"
    company = Register.objects.get(c_email = email)
    data = Product_Hardware.objects.filter(p_company_id = company.id)
    for i in range(0,len(data)):
        InWishlist = Wishlist.objects.filter(product_name__iexact=data[i],user_email__iexact=request.user.email).exists()
        InCart = Cart.objects.filter(product_name__iexact=data[i].p_name, user_email__iexact=request.user.email).exists()
        data[i].inWishlist = InWishlist
        data[i].inCart = InCart

    return render(request, temp, {'data':data, 'CompanyName':company.c_name, 'CompanyEmail':company.c_email})

def Product_Details_View(request, ID):
    temp = "User/product_details.html"
    data = Product_Hardware.objects.get(id = ID)
    category = Product_Catagory.objects.get(id = data.p_catagory_id)
    review_form = Product_Review_form()
    review_data = Product_Review.objects.filter(product_id = ID)
    InWishlist = Wishlist.objects.filter(product_name__iexact=data.p_name, user_email__iexact=request.user.email).exists()
    InCart = Cart.objects.filter(product_name__iexact=data.p_name, user_email__iexact=request.user.email).exists()
    return render(request, temp, {'data':data, 'categoryName':category.catagory_name, 'review_form':review_form, 'review_data':review_data, 'inWishList':InWishlist, 'inCart':InCart})

def Add_Product_Review_View(request):
    product_id = request.POST.get('product_id')
    product_name = request.POST.get('product_name')
    if request.method == "POST":
        print("In post form")
        review_form = Product_Review_form(request.POST or None)
        print("form get")
        product = Product_Hardware.objects.get(id = product_id)
        user_id = request.user
        user_name = request.user.username
        user_email = request.user.email
        if review_form.is_valid():
            print("form Valid")
            form = review_form.save(commit=False)
            form.product = product
            form.product_name = product_name
            form.user = user_id
            form.user_name = user_name
            form.user_email = user_email
            review_form.save()
            return redirect(reverse('User:Product_Details', args=(product_id,)))
        else:
            print("form not valid")
    else:
        print("get")
        return redirect('User:All_Company')



def User_Wishlist_View(request):
    temp = "User/wishlist.html"
    data = Wishlist.objects.filter(user= request.user).order_by('-added_in_wishlist')
    return render(request, temp, {'data':data})

def User_Cart_View(request):
    temp = "User/cart.html"
    data = Cart.objects.filter(user=request.user).order_by('-added_in_cart')
    TOTAL = 0
    for i in range(0, len(data)):
        TOTAL = TOTAL + float(data[i].sub_total)
    print(TOTAL)
    return render(request, temp, {'data':data, 'TOTAL':TOTAL})


def My_Bookings_View(request):
    temp = "User/bookings.html"
    data = Bookings.objects.filter(user_id = request.user.id).order_by('-order_no_id')
    for i in range(0,len(data)):
        ORDER = Order_No_For_User.objects.filter(id = data[i].order_no_id)
        data[i].ORDER_NO = ORDER[0].order_no
    return render(request, temp, {'data':data})