from django.shortcuts import render,redirect    
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html') 
def registeration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['e-mail']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect('registeration')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save();
                messages.info(request,"User created")
                return redirect('registeration')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('registeration')
        return redirect('login')
    else:
        
        return render(request,'register.html')