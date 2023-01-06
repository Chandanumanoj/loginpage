from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import*
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.contrib import messages


@never_cache
def base_file(request):
    if 'username' in request.session:
        return render(request,'authentication/base_file.html')
    else:
        return redirect('user_login')
@never_cache
def user_login(request):
    if 'username' in request.session:
        return redirect('base_file')
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['username']=username
            return redirect('base_file')
        else:
            messages.info(request,'invalid credentials')
            
    return render(request,'authentication/user_login.html')            


def user_logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('user_login')    




