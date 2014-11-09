#coding: utf-8
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from models import Tour


def landing_render(request):
    return render(request, 'index.html', {"tours": Tour.objects.all()})


def send_order(request):
    if request.method == 'POST':
        if request.POST["phone"]:
            message = 'от ' + request.POST.get('name') + '. Телефон: ' + request.POST.get('phone','')
            print(message)
            send_mail(
                'Новая заявка c BrokerTour',
                message,
                request.POST.get('email', ''),
                ['ipavelleds@gmail.com'],
                fail_silently=False
            )
            print "Mail send"
            return redirect('/')
    print "Mail not send"
    return redirect('/')