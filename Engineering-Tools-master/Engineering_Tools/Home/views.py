from django.shortcuts import render

# Create your views here.

def Home_Route_View(request):
    Temp = "Home_route.html"
    return render(request, Temp)