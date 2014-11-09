#coding: utf-8
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from models import Tour


def landing_render(request):
    return render(request, 'index.html', {"tours": Tour.objects.all()})


def send_order(request):
    current_tour = Tour.objects.all()[int(request.POST.get('tour-id'))-1]
    user_name = ""
    user_email = ""
    if request.method == 'POST':
        if request.POST["phone"]:
            if request.POST["name"]:
                user_name = u'Имя клиента: ' + request.POST["name"] + '\n'
            if request.POST["email"]:
                user_email = u'Почта клиента: ' + request.POST["email"] + '\n'
            message = user_name + user_email + u'Выбран тур: ' + current_tour.nameTour
            send_mail(
                'Новая заявка c BrokerTour',
                message,
                request.POST['email'],
                ['ipavelleds@gmail.com'],
                fail_silently=False
            )
            return redirect('/')
    return redirect('/')