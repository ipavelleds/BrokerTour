#coding: utf-8

from django.db import models


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