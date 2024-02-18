from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import get_user_model,authenticate,login,logout


User=get_user_model()

def register(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('username taken')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('email already in use')
            user=User.objects.create_user(username=username,password=password1,email=email)
            user.save()
        else:
            context={
                'error':'password not matching'
            }
            return render (request,'registration/register.html',context)
            
        print('user created')
        return redirect('/accounts/login')
        
    else:
        return render (request,'registration/register.html')
    
    
def log_in(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            context={
                'error':'username/password incorrect'
            }
            return render (request,'registration/login.html',context)

    else:
        return render (request,'registration/login.html')
    
    
def log_out(request):
    logout(request)
    return redirect('/')