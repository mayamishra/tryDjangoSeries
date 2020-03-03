from django.shortcuts import render
from django.http import HttpResponse

def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html",{})
    #return HttpResponse("<h1>Hello World</h1>")

def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})
    
def about_view(request,*args,**kwargs):
    my_context={"title":"abc This is about us", 
    "this_is_true":True,
    "my_number":123,
    "my_list":[123,434,312,"Abc"],
    "my_html": "<h1> Hello World </h1>"
    }
    return render(request,"about.html", my_context)

def social_view(request,*args,**kwargs):
    return HttpResponse("<h1>Social Page</h1>")


# Create your views here.
