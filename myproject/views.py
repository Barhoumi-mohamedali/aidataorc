# Import render module from django
from django.shortcuts import render
from datetime import datetime
now = datetime.now()
from django.shortcuts import  render, redirect
from django.contrib.auth import logout
from django.conf import settings


from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create index function to display the HTML file into the browser
def index(request):
    return render(request, "index.html",
			{
			    'title' : "Web Data Platform",
			    'message' : "Hello Web Data Platform!",
			    'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
			}

    )
def login_request(request):
 if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')
       user = authenticate( username=username, password=password)
       if user is not None:
          login(request, user)
          messages.info(request, f"You are now logged in as {username}.")
          return render(request, 'home.html') 
       else:
           messages.error(request,"Invalid username or password.")
    else:
          messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    #return render(request,"login.html", context={"login_form":form})    
 return render(request, "login.html",
			{
 			    'title' : "Web Data Platform",
 			    'message' : "Hello Web Data Platform!",
 			    'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
 			}
 
     )
def logout_view(request):
    logout(request)
    return render(request, "index.html")
def home(request):
     if not request.user.is_authenticated:
          return render(request, "login.html")
     return render(request, "home.html")
def ocr(request):
    if not request.user.is_authenticated:
                  return render(request, 'login.html')
    return render(request, "product/ocr.html",
			{
			    'title' : "Web Data Platform",
			    'message' : "Hello OCR !",
			    'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
			}

    )
