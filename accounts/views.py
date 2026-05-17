import random

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect


generated_otp = ""


def login_page(request):

    global generated_otp

    if request.method == 'POST':

        email = request.POST.get('email')
        entered_otp = request.POST.get('otp')

        if entered_otp:

            if entered_otp == generated_otp:
                return redirect('/dashboard/')

        else:

            generated_otp = str(random.randint(100000, 999999))

            send_mail(
                'Your OTP Code',
                f'Your OTP is: {generated_otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return render(request, 'login.html', {
                'email': email
            })

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def firstmbbs(request):
    return render(request, 'firstmbbs.html')
def faculty(request):
    return render(request, 'faculty.html')
def department(request, dept_name):

    context = {

        'department': dept_name

    }

    return render(
        request,
        'anatomy.html',
        context
    )
