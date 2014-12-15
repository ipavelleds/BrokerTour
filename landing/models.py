#coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from mixins import ModelDiffMixin


class Tour(models.Model):
    picture = models.ImageField(upload_to="img_tours", verbose_name="Изображение тура")
    nameTour = models.CharField(max_length=250, verbose_name="Название тура")
    time = models.CharField(max_length=250, verbose_name="Время проживания")
    dateDeparture = models.CharField(max_length=250, verbose_name="Дата тура")
    nameHotel = models.CharField(max_length=250, verbose_name="Название гостиницы")
    aboutHotel = models.CharField(max_length=250, verbose_name="Тип питания в гостинице")
    starHotel = models.IntegerField(verbose_name="Кол-во звезд рейтинга гостиницы")
    piece = models.IntegerField(verbose_name="Цена тура")

    def get_stars(self):
        return range(self.starHotel)

    def get_piece(self):
        piece = str(self.piece)[:-3] + u' ' + str(self.piece)[-3:]
        return piece

    def __unicode__(self):
        return self.nameTour


class Proposal(models.Model, ModelDiffMixin):
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    name = models.CharField(max_length=400, verbose_name="Имя клиента", blank=True, null=True)
    email = models.EmailField(max_length=200, verbose_name="Емайл", blank=True, null=True)
    tour = models.ForeignKey(Tour, verbose_name="Выбранный тур", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.phone

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.has_changed:
            is_instance_updated = True
            if not self.id:
                is_instance_updated = False
            super(Proposal, self).save(force_insert=force_insert, force_update=force_update, using=using,
                 update_fields=update_fields)
            self.send_email_to_admins(is_instance_updated)

    def send_email_to_admins(self, is_instance_updated=False):
        super_users = User.objects.filter(is_superuser=True)
        recipients = [super_user.email for super_user in super_users]
        if not recipients:
            recipients = [settings.EMAIL_HOST_USER]
        if not is_instance_updated:
            subject = 'Новая заявка на BrokerTur.com'
            message = u'Телефон клиента: ' + self.phone + u'\nВыбран тур: ' + self.tour.nameTour
        else:
            user_name = u'Имя клиента: ' + self.name + '\n' if self.name else ""
            user_email = u'Почта клиента: ' + self.email + '\n' if self.email else ""
            subject = 'Заявка, поданная ранее на BrokerTur.com, была обновлена'
            message = user_name + user_email + u'Телефон клиента: ' + self.phone + u'\nВыбран тур: ' + self.tour.nameTour
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipients,
            fail_silently=False
        )