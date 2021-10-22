from django.urls import path, re_path
from .views import hayvan_girisi, hayvan_listesi, hayvan_detay, hayvan_sil, hayvan_guncelle

urlpatterns = [
    path('hayvan-girisi/', hayvan_girisi, name='hayvan-girisi'),
    path('hayvan-listesi/', hayvan_listesi, name='hayvan-listesi'),
    re_path(r'hayvan-detay/(?P<pk>[0-9]+)/$', hayvan_detay, name='hayvan-detay'),
    re_path(r'hayvan-sil/(?P<pk>[0-9]+)/$', hayvan_sil, name='hayvan-sil'),
    re_path(r'hayvan-guncelle/(?P<pk>[0-9]+)/$', hayvan_guncelle, name='hayvan-guncelle'),
]
