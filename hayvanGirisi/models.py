from django.db import models
from django.shortcuts import reverse

# Create your models here.

class HayvanGiris(models.Model):
    PADOKNO = (
    (None, 'Padok No Seçiniz'), ('padokno1', 'Padok No1'), ('padokno2', 'Padok No2'), ('padokno3', 'Padok No3'))
    IRK = ((None, 'Irk Seçiniz'), ('montofon', 'Montofon'), ('holstein', 'Holstein'), ('simentol', 'Simentol'),
           ('jersey', 'Jersey'), ('angus', 'Angus'))
    CINSIYET = ((None, 'Cinsiyet Seçiniz'), ('erkek', 'Erkek'), ('duve', 'Düve'),('inek','İnek'),('malak','Malak'))
    ISLETME = (
    (None, 'İşletme Seçiniz'), ('isletme1', 'İşletme 1'), ('isletme2', 'İşletme 2'), ('isletme3', 'İşletme 3'))
    kupe_no = models.CharField(max_length=50, verbose_name='Küpe No', blank=True, null=True, unique=True)
    pasaport_no = models.CharField(max_length=50, verbose_name='Pasaport No', blank=True, null=True,unique=True)
    padok_no = models.CharField(choices=PADOKNO, verbose_name='Padok No', max_length=50, blank=False, null=True)
    irki = models.CharField(choices=IRK, verbose_name='IRK', max_length=50, blank=False, null=True)
    alis_fiyati = models.CharField(max_length=50, verbose_name='Alış Fiyatı', blank=False, null=True)
    satis_fiyati = models.CharField(max_length=50, verbose_name='Satış Fiyatı', blank=True, null=True)
    alis_kg = models.CharField(max_length=50, verbose_name='Alış Kg', blank=True, null=True)
    alis_tarihi = models.DateField(null=True, blank=True, verbose_name='Alış Tarihi')
    cinsiyet = models.CharField(choices=CINSIYET, blank=False, null=True, max_length=20, verbose_name='Cinsiyet')
    isletme = models.CharField(choices=ISLETME, verbose_name='ISLETME', max_length=50, blank=False, null=True)
    aciklama = models.TextField(max_length=1000, verbose_name='Açıklama', blank=True, null=True)
    alici_bilgi = models.TextField(max_length=1000, verbose_name='Alıcı Bilgi', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Hayvan'

    def get_absolute_url(self):
        return reverse('hayvan-detay', kwargs={'pk': self.pk})

    def __str__(self):
        return (self.pk)