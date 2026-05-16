from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_page(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')
def firstmbbs(request):
    return render(request, 'firstmbbs.html')
