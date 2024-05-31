from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from userauthentication.models import user_db
from django.contrib.auth.decorators import login_required


# Create your views here.

#register page
def register(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          email = request.POST.get('email')
          password = request.POST.get('password')
          confirm_password = request.POST.get('confirm_password')
          profile_pic = request.FILES.get('profile_pic')

          if user_db.objects.filter(username=username).exists():
               messages.error(request, "User already exist.")
          elif user_db.objects.filter(email=email).exists():
               messages.error(request, "Email is already exist.")
          elif password != confirm_password:
               messages.error(request, "password not matched!")
          else:
               useracc = user_db.objects.create(
                    username=username,
                    email=email,
                    password=password
               )
               if profile_pic:
                    useracc.profile_pic = profile_pic
                    useracc.save()
                    messages.success(request, "You are successfull register.")
                    return redirect('/login/')
               
     return render(request, 'home/register.html' )

#login page
def login(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          if not user_db.objects.filter(username=username).exists():
               messages.error(request, "User not found.")
               return redirect('/login/')

          else:
               user = authenticate(request, username=username, password=password)

               if not user is None:
                    messages.error(request, "Password is incorrect")
                    return redirect('/login/')
               else:
                    auth_login(request, user)
                    return redirect('/')

     return render(request, 'home/login.html')

#profile page
@login_required
def profile(request):
     all_ = user_db.objects.filter(id=request.user.id).order_by('-date')
     context = {'all_': all_}
     return render(request, 'home/profile.html', context)



