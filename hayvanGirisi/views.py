from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, HttpResponseRedirect, reverse
from .forms import HayvanGirisiForm, HayvanAra
from .models import HayvanGiris
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import HayvanForm, HayvanGirisiForm


# Create your views here.

def hayvan_girisi(request):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    form = HayvanGirisiForm()
    if request.method == "POST":
        deger = request.POST.__str__()
        print(deger)
        form = HayvanGirisiForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            msg = "%s küpe nolu hayvan başarıyla girildi." % (form_save.kupe_no)
            messages.success(request, msg, extra_tags='success')
            return HttpResponseRedirect(form_save.get_absolute_url())
        else:
            print('Not valid')
    return render(request, 'hayvanGirisi/hayvan-girisi.html', context={'form': form})


def hayvan_listesi(request):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    gelen_deger = request.GET.get('id', None)
    hayvanlar = HayvanGiris.objects.all()
    form = HayvanAra(data=request.GET or None)
    if form.is_valid():
        search = form.cleaned_data.get('search', None)
        if search:
            hayvanlar = hayvanlar.filter(
                Q(kupe_no__icontains=search) | Q(pasaport_no__icontains=search) | Q(irki__icontains=search))
    page = request.GET.get('page', 1)
    if gelen_deger:
        hayvanlar = hayvanlar.filter(id=gelen_deger)
    paginator = Paginator(hayvanlar, 8)
    try:
        hayvanlar = paginator.page(page)
    except EmptyPage:
        hayvanlar = paginator.page((paginator.num_pages))
    except PageNotAnInteger:
        hayvanlar = paginator.page(1)
    return render(request, 'hayvanGirisi/hayvan-listesi.html', context={'hayvanlar': hayvanlar, 'form': form})


def hayvan_detay(request, pk):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    form = HayvanGirisiForm
    try:
        hayvan = HayvanGiris.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, 'hayvanGirisi/hayvan-detay.html', context={'hayvan': hayvan, 'form': form})


def hayvan_sil(request, pk):
    hayvan = get_object_or_404(HayvanGiris, pk=pk)
    hayvan.delete()
    return HttpResponseRedirect(reverse('hayvan-listesi'))


def hayvan_guncelle(request, pk):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    hayvan = get_object_or_404(HayvanGiris, pk=pk)
    form = HayvanGirisiForm(instance=hayvan, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form_save = form.save()
        return HttpResponseRedirect(reverse('hayvan-detay', kwargs={'pk': form_save.pk}))
    context = {'form': form, 'hayvan': hayvan}
    return render(request, 'hayvanGirisi/hayvan-guncelle.html', context=context)
