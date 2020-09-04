from django.urls import path
from .views import Home_View_User,My_Account_View, Update_Account_Info_View, All_Company_View, All_Product_By_Company, Product_Details_View, Add_Product_Review_View, User_Wishlist_View, User_Cart_View, My_Bookings_View

app_name = "User"

urlpatterns = [
    path('', Home_View_User, name="Home"),
    path('Account', My_Account_View, name="My_Account"),
    path('Update_Account', Update_Account_Info_View, name="Update_Account"),
    path('All_Company', All_Company_View, name="All_Company"),
    path('Products_By_Company/<str:email>', All_Product_By_Company, name="All_Product_By_Company"),
    path('Product_Details/<int:ID>', Product_Details_View, name="Product_Details"),
    path('Add_Product_Review', Add_Product_Review_View, name="Product_Review"),
    path('Wishlist', User_Wishlist_View, name="Wishlist"),
    path('Cart', User_Cart_View, name="Cart"),
    path('My_Bookings', My_Bookings_View,name="Bookings"),

]
