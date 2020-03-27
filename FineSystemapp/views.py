from django.shortcuts import render
from FineSystemapp.forms import New_3FineApply
from FineSystemapp.forms import New_1Rules_Add
from .models import Apply_Fine
from django.db.models import Sum
from django.core.mail import send_mail
from Finesystem import settings
# Create your views here.
def Home(request):
    return render(request, 'FineSystemapp/index.html')

def My_rules(request):
    return render(request, 'FineSystemapp/My_Rules.html')
def Apply_Fine_View(request):
    form = New_3FineApply()
    if request.method == 'POST':
        form = New_3FineApply(request.POST)

        if form.is_valid():
            form.save(commit=True)
            subject = 'Fine System :IV Pillar'
            msg='You have apllied with the Fine for more detail please visit FIne System'
            to=['snehgour80@gmail.com','dubeybulbul111@gmail.com']
            res=send_mail(subject,msg,settings.EMAIL_HOST_USER,to)
            if res==1:
                msg='Mail sent'
                return Home(request)
        else:
            print("ERROR FROM INVALID")
    return render(request, 'FineSystemapp/Fine_Apply.html', {'form': form})


def Add_Rules(request):
    form = New_1Rules_Add()
    if request.method == 'POST':
        form = New_1Rules_Add(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return Apply_Fine(request)
        else:
            print("ERROR FROM INVALID")
    return render(request, 'FineSystemapp/Add_Rules.html', {'form': form})

def dashboard_view(request):
    total_fine=Apply_Fine.objects.aggregate(Sum('Fine_Amount')) 
    sneh_fine=Apply_Fine.objects.filter(Username='snehgour80@').aggregate(Sum('Fine_Amount'))
    jahanvi_fine=Apply_Fine.objects.filter(Username='dubeybulbul111@').aggregate(Sum('Fine_Amount'))
    context={'total_fine':total_fine,'sneh_fine':sneh_fine,'jahanvi_fine':jahanvi_fine}
    return render(request,'FineSystemapp/Dashboard.html',context)


def about_us_view(request):
    return render(request,'FineSystemapp/About_us.html')

