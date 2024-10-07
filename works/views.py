from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServForm, WorkForm
from .models import Serv, Work


def authorization(request):
    return render(request, 'works/authorization.html')


@login_required(login_url="authorization")
def home_page(request):
    ser = Serv.objects.all()
    w = Work.objects.all()
    context = {'ser': ser,
               'work': w}
    return render(request, 'works/home_page.html', context)


@login_required(login_url="authorization")
def add_service(request):
    form = ServForm()

    if request.method == "POST":
        form = ServForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, 'works/add_service.html', context)


@login_required(login_url="authorization")
def add_work(request):
    form = WorkForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('home-page')

    context = {'form': form}
    return render(request, 'works/add_work.html', context)


@login_required(login_url="authorization")
def delete_service(request, pk):
    serv = Serv(id=pk)

    if request.method == "POST":
        serv.delete()
        return redirect("home-page")
    context = {'object': serv}
    return render(request, 'works/delete_service.html', context)


@login_required(login_url='authorization')
def update_service(request, pk):
    serv = Serv(id=pk)
    form = ServForm(instance=serv)

    if request.method == "POST":
        form = ServForm(request.POST, instance=serv)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'serv': serv, 'form': form}
    return render(request, 'works/add_service.html', context)


@login_required(login_url='authorization')
def result(request):
    wr = Work.objects.all()
    s = 0
    zp = 0
    ost = 0
    for w in wr:
        s += w.price
    if request.method == "POST":
        summ = request.POST.get('sum')
        kl = request.POST.get('kl')
        zp = int(summ) * 0.4 / int(kl)
        ost = int(summ) - (zp * int(kl))
    context = {'sum': s, 'zp': zp, 'ost': ost}
    return render(request, 'works/result.html', context)


@login_required(login_url='authorization')
def reset(request):
    wr = Work.objects.all()
    if request.method == "POST":
        wr.delete()
        return redirect("home-page")
    return render(request, 'works/reset.html')
