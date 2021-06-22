from app.models import Feedback
from django.shortcuts import redirect, render
from app.forms import FeedbackForm
from app.models import Product
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def feedback_form(request):
    
    form = FeedbackForm()
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Thanks for feedback!!')
            return redirect('/overview/')


    return render(request,"feedbackform.html",{"form":form})


def home(request):

    all_product=Product.objects.all()
    return render(request,'home.html',{'all_product':all_product})

@login_required
def overview(request):
    all_feedback=Feedback.objects.all()
    return render(request,"overview.html",{"all_feedback":all_feedback})



def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.save();
            messages.info(request,"User Created!!")
        
        else:
            messages.info(request,'Password not mached!!')
            return redirect("/register")
        return redirect("/login")
    else:    
        return render(request,"register.html")


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        else:   
            messages.info(request,'Wrong Username or Password !!')
            return redirect('/login')   
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/home')
