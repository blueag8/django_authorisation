from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from auth_py.forms import UserLoginForm
# Create your views here.
def index(request):

    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have succesfully logged out")
    return redirect(reverse('index'))

def login(request):

    if request.method=="POST":
        login_form=UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username= request.POST['username'],
                                     password= request.POST['password'])
            messages.success(request, "You have successfully logged in ")
            if user:
               auth.login(user=user, request=request)
            else:
                login_form.add_error(None, "Your username or password is incorrect")

    else:
        login_form= UserLoginForm()
    return render(request, 'login.html', {'login_form':login_form})