from django.contrib import messages
from django.shortcuts import redirect, render
from .models import searchModel
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import patient_form
from django.contrib.auth import authenticate


# from django.contrib.auth.decorators import login_required
# @login_required


# Create your views here.

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def privacy(request):
    return render(request ,'pages/privacy.html')


def our_services(request):
    ser=searchModel.objects.all()
    service={'ser':ser.order_by('name')}
    return render(request,'pages/our_services.html',service)

def our_team(request):
    return render(request,'pages/our_team.html')


def privacy(request):
    return render(request,'pages/privacy.html')

def profile(request):

    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        form=patient_form(request.POST or None,instance=current_user)
        if form.is_valid():
            form.save()
            login(request,current_user)
            messages.success(request,"Your Profile Has Been Successfully Updated!")
            return redirect('home')

        return render(request,'pages/profile.html',{'form':form})
    
    else:
        messages.success(request,("You must login first"))
        return redirect('home')


def search(request):

    if request.method=="POST":
         searched=request.POST.get('searched',False)
         searches=searchModel.objects.filter(name=searched)
         return render(request,'pages/search.html',{'searched':searched,'searches':searches})
    
    else:
         return render(request,'pages/search.html')
