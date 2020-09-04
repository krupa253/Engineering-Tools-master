from django.urls import path
from .views import ET_login, ET_Home, ET_All_Company, ET_Product_Category, ET_All_User, ET_All_Feedback, ET_logout, ET_logout_done, ET_All_Hardware, ET_All_Software
app_name = 'Admin'

urlpatterns = [
    path('',ET_login, name="Admin_login"),
    path('Logout/',ET_logout, name="Admin_logout"),
    path('Logout_done/',ET_logout_done, name="Admin_logout_done"),
    path('Home/', ET_Home, name="Admin_home"),
    path('Companies/', ET_All_Company, name="Admin_company"),
    path('Categories/', ET_Product_Category, name="Admin_category"),
    path('Users', ET_All_User, name="Admin_user"),
    path('Feedbacks', ET_All_Feedback, name="Admin_feedback"),
    path('Hardwares', ET_All_Hardware, name="Admin_hardware"),
    path('Softwares', ET_All_Software, name="Admin_software"),
]