from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    context = {"name" : "test"}
    return render(request,"home.html", context=context )