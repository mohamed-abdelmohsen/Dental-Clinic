from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from project import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .tokens import generate_token



# Create your views here.

def hello(request):
    return render(request,'authentication/hello.html')

def signup(request):

    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']


        if User.objects.filter(username=username):
            messages.error(request,'username already exists')
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request,'Email already registered')
            return redirect('signup')
        
        if len(username)>10:
            messages.error(request,'username is too long')

        if pass1 != pass2:
            messages.error(request,"Passwords don't match")

        if not username.isalnum:
            messages.error(request,'username must be Alpha-Numeric')
            return redirect('signup')


        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.is_active = False
        myuser.save()

        messages.success(request,"Your Account have been successfully created, we have sent you confirmation email")

        # Welcome email
        subject="Welcome to teeth lap - django admin"
        message="hello , " + myuser.first_name +"\n Thanks For Visiting Our Website . \n We Hope You Speedy Recovery , God Willing ."
        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)


        # Email address configration email

        current_site=get_current_site(request)
        email_subject="Confirm your email "
        message2=render_to_string('email_configration.html',{
            'name':myuser.first_name,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),

        })
        
        email=EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser,email],
        )
        email.fail_silently=True
        email.send()

        return redirect("signin")


    return render(request,'authentication/signup.html')


def signin(request):

    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user= authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'pages/home.html',{'fname':fname})


        else:
            messages.error(request,'Bad Credentials')
            return redirect('hello')

    return render(request,'authentication/hello.html')

def signout(request):
    logout(request)
    messages.error(request,'Logged out successfully')
    return redirect('hello') 



def activate(request , uidb64, token):
    try :
        uid=force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser=None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active=True
        myuser.save()
        login(request,myuser)
        return redirect('hello')

    else:
        return render(request,'activation_failed.html')
    
