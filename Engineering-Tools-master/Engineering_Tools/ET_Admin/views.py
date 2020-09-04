from django.shortcuts import render, redirect
from Company.models import Company_Profile, Product_Catagory
from django.contrib.auth.models import User


# Create your views here.
def ET_login(request):
    if request.session.get('Admin') != None:
        return redirect("Admin:Admin_home")
    temp = "ET_Admin/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print('\n')
        print(password)

        if username == "Admin" and password == "Admin":
            print("Admin Login Done")
            request.session['Admin'] = 'True'
            return redirect("Admin:Admin_home")
        else:
            print("Username and password not match, Login Fail")

    return render(request,temp)



def ET_logout(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")

    temp = "ET_Admin/logout.html"
    return render(request, temp)


def ET_logout_done(request):
    if request.session.get('Admin') != None:
        request.session.delete()
        return redirect("Admin:Admin_login")
    else:
        return redirect("Admin:Admin_login")



def ET_Home(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")
    temp = "ET_Admin/index.html"
    return render(request,temp)



def ET_All_Company(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")
    temp = "ET_Admin/all_company.html"
    data = Company_Profile.objects.all()
    return render(request, temp, {'company':data})



def ET_Product_Category(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")
    temp = "ET_Admin/all_categories.html"
    data = Product_Catagory.objects.all()
    return render(request, temp, {'category':data})



def ET_All_User(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")
    temp = "ET_Admin/all_user.html"
    data = User.objects.all()
    return render(request, temp, {'user':data})



def ET_All_Feedback(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")
    temp = "ET_Admin/all_feedback.html"
    data = User.objects.all()
    return render(request, temp, {'user':data})


def ET_All_Hardware(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")
    temp = "ET_Admin/all_hardware.html"
    data = User.objects.all()
    return render(request, temp, {'user':data})



def ET_All_Software(request):
    if request.session.get('Admin') == None:
        return redirect("Admin:Admin_login")
    temp = "ET_Admin/all_software.html"
    data = User.objects.all()
    return render(request, temp, {'user':data})
