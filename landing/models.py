from django.db import models


class Tour(models.Model):
    picture = models.ImageField(upload_to="img_tours")
    nameTour = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    dateDeparture = models.CharField(max_length=250)
    nameHotel = models.CharField(max_length=250)
    aboutHotel = models.CharField(max_length=250)
    starHotel = models.IntegerField()
    piece = models.IntegerField()

    def get_stars(self):
        return range(self.starHotel)
