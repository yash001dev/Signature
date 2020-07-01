from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,User
from .decorators import unauthenticated_user,allowed_users,admin_only
from .models import *
from .form import CreateUserForm,LoginForm
# Create your views here.
@unauthenticated_user   
def login(request):
    form=LoginForm(request.POST)
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password1')
        print(username)
        print(password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')
        
        else:
            messages.info(request,'Username and Password is Incorrect')
        
    context={'form':form}
    return render(request,'login.html',context)
    
def home(request):
    return render(request,'index.html')
@unauthenticated_user
def signup(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='Student')
            user.groups.add(group)
            user=form.cleaned_data.get('username')
            messages.success(request,'Account Was Created For'+user)
            return redirect('login')
        else:
            messages.info(request,'Your Details is Incorrect')
    context={'form':form}
    return render(request,'signup.html',context)

def logOut(request):
    logout(request)
    return redirect('login')

@login_required(login_url='loginPage')
def dashboard(request):
    return render(request,'dashboard3.html')

@login_required(login_url='loginPage')
def user_data(request):
    if request.method=="POST":
        Name=request.POST['Name']
        ItselfIntro=request.POST['ItselfIntro']
        AdventureIntro=request.POST['AdventureIntro']
        SkillsIntro=request.POST['SkillsIntro']
        JobIntro=request.POST['JobIntro']
        SchollingIntro=request.POST['SchollingIntro']
        ContactIntro=request.POST['ContactIntro']
        data=UserData.objects.create(
        user=request.user,
        Name=Name,
        ItselfIntro=ItselfIntro,
        AdventureIntro=AdventureIntro,
        SkillsIntro=SkillsIntro,
        JobIntro=JobIntro,
        SchollingIntro=SchollingIntro,
        ContactIntro=ContactIntro
        )
        context={
        "Name":Name,
        "ItselfIntro":ItselfIntro,
        "AdventureIntro":AdventureIntro,
        "SkillsIntro":SkillsIntro,
        "JobIntro":JobIntro,
        "SchollingIntro":SchollingIntro,
        "ContactIntro":ContactIntro
        }
        return render(request,'signature/bio1.html',context) 
    return render(request,'user_data.html',)

# @unauthenticated_user
def bio(request,username):
    # userdata=User.objects.filter(username=username)    
    # print(userdata)
    maindata=UserData.objects.filter(user=User.objects.get(username=username))

    print("maindata")
    # print(maindata[0].use)
    context={
        "Name":maindata[0].Name,
        "ItselfIntro":maindata[0].ItselfIntro,
        "AdventureIntro":maindata[0].AdventureIntro,
        "SkillsIntro":maindata[0].SkillsIntro,
        "JobIntro":maindata[0].JobIntro,
        "SchollingIntro":maindata[0].SchollingIntro,
        "ContactIntro":maindata[0].ContactIntro
        }
    return render(request,'signature/bio1.html',context)

def handler404(request):
    return render(request, '404.html', status=404)
    
def handler500(request):
    return render(request, '404.html', status=500)