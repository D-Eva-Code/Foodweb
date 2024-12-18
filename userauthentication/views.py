from django.shortcuts import render,redirect
from .forms import Registerform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile
# Create your views here.

def register(request):
    if request.method =="POST":
        form = Registerform(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, your account has been created")
            return redirect("login")
    
    else:
        form = Registerform()
    return render(request, "register.html",{"form":form})

# def Loginview(request):
#     if request.method == POST:
@login_required
def LogoutView(request):
    if request.method == "POST":
        logout(request)
        return render(request, "logout.html")
    else:
        return render(request, "logout.html")

@login_required        
def profile(request):
        # try:
        #     profile = request.user.profile
        # except Profile.DoesNotExist:
        # # Optionally create a profile if missing
        #     profile = Profile.objects.create(user=request.user)
        return render(request, 'profile.html')
