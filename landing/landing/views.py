from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def landing_page(request):
    return render(request, 'landing/landing_page.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')
            # return render(request, 'landing/landing_page.html')
        else:
            return redirect('login')    
            # return render(request, 'landing/login.html') 
    elif request.method == 'GET':
        return render(request, 'landing/login.html')    
