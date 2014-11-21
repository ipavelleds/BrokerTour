#coding: utf-8
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from models import Tour
from django.contrib.auth.models import User


def landing_render(request):
    return render(request, 'index.html', {"tours": Tour.objects.all()})


def send_order(request):
    super_users = User.objects.filter(is_superuser=True)
    recipients = [super_user.email for super_user in super_users]
    if recipients == [u'']:
        recipients = [settings.EMAIL_HOST_USER]
    current_tour = Tour.objects.all()[int(request.POST.get('tour-id'))-1]
    user_name = ""
    user_email = ""
    if request.method == 'POST':
        if request.POST["phone"]:
            if request.POST["name"]:
                user_name = u'Имя клиента: ' + request.POST["name"] + '\n'
            if request.POST["email"]:
                user_email = u'Почта клиента: ' + request.POST["email"] + '\n'
            message = user_name + user_email + u'Телефон клиента: ' + request.POST["phone"] + u'\nВыбран тур: ' + current_tour.nameTour
            send_mail(
                'Новая заявка c BrokerTour',
                message,
                settings.EMAIL_HOST_USER,
                recipients,
                fail_silently=False
            )
            return redirect('/')
    return redirect('/')