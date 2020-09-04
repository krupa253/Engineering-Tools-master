from django.urls import path
from .views import Home_View_Company, Register_view, Login_view, Logout_view,Add_profile_view , Add_new_password, Forgot_password, Otp_match, Show_profile_view, Edit_profile_view, Account_verification_view, Please_verify_view, Product_Hardware_view, Account_verification_done, Logout_done, Product_Software_view, All_Hardware_product_view, All_Software_product_view, Hardware_Details_view, Software_Details_view, Edit_Hardware_product_view, Edit_Software_product_view, Delete_Hardware_product_view, Delete_Software_product_view
app_name = "Company"

urlpatterns = [
    path('Home', Home_View_Company, name="Home"),
    path('Register', Register_view, name="Register"),
    path('Verify', Please_verify_view, name="Please_verify"),
    path('Verification', Account_verification_view, name="Verification"),
    path('Verification_done', Account_verification_done, name="Verification_done"),
    path('Login', Login_view , name="Login"),
    path('Logout', Logout_view , name="Logout"),
    path('Logout_done', Logout_done , name="Logout_done"),
    path('Profile',Show_profile_view,name="Show_profile"),
    path('Add_profile', Add_profile_view , name="Add_profile"),
    path('Edit_profile/<int:pk>', Edit_profile_view , name="Edit_profile"),
    path('Forgot_password', Forgot_password, name="Forgot_password" ),
    path('Add_new_password', Add_new_password, name="Add_New_Password" ),
    path('Enter_otp', Otp_match, name="Enter_otp" ),
    path('Add_hardware_product', Product_Hardware_view, name="Add_Hardware_product"),
    path('Add_software_product', Product_Software_view, name="Add_Software_product"),
    path('All_hardware_product', All_Hardware_product_view, name="All_Hardware_product"),
    path('All_software_product', All_Software_product_view, name="All_Software_product"),
    path('Hardware_details/<str:no>', Hardware_Details_view, name="Hardware_details"),
    path('Software_details/<str:name>', Software_Details_view , name="Software_details"),
    path('Edit_Hardware/<int:productId>', Edit_Hardware_product_view , name="Edit_Hardware"),
    path('Edit_Software/<int:productId>', Edit_Software_product_view, name="Edit_Software"),
    path('Delete_Hardware', Delete_Hardware_product_view, name="Delete_Hardware"),
    path('Delete_Software', Delete_Software_product_view, name="Delete_Software"),
]
