from django import forms
from .models import HayvanGiris
import datetime

cur_year = datetime.datetime.today().year
year_range = tuple([i for i in range(cur_year - 20, cur_year + 2)])


class HayvanGirisiForm(forms.ModelForm):
    alis_tarihi = forms.DateField(widget=forms.SelectDateWidget(years=year_range))

    class Meta:
        model = HayvanGiris
        fields = ['kupe_no', 'pasaport_no', 'padok_no', 'irki', 'alis_fiyati', 'satis_fiyati', 'alis_kg', 'alis_tarihi',
                  'cinsiyet', 'isletme', 'aciklama', 'alici_bilgi']

    def __init__(self, *args, **kwargs):
        super(HayvanGirisiForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['aciklama'].widget.attrs['rows'] = 10
        self.fields['alici_bilgi'].widget.attrs['rows'] = 10


class HayvanAra(forms.Form):
    search = forms.CharField(required=False, max_length=500, widget=forms.TextInput(
        attrs={'placeholder': 'Hayvanlarda arayın', 'class': 'form-control'}))


class HayvanForm(forms.ModelForm):
    class Meta:
        model = HayvanGiris
        fields = ['kupe_no', 'pasaport_no', 'alis_fiyati', 'satis_fiyati']

    def __init__(self, *args, **kwargs):
        super(HayvanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
