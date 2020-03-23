from django.shortcuts import render
from FineSystemapp.forms import New_3FineApply
from FineSystemapp.forms import New_1Rules_Add


# Create your views here.
def Home(request):
    return render(request, 'FineSystemapp/index.html')

def My_rules(request):
    return render(request, 'FineSystemapp/My_Rules.html')
def Fine_Apply(request):
    form = New_3FineApply()
    if request.method == 'POST':
        form = New_3FineApply(request.POST)

        if form.is_valid():
            form.save(commit=True)
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
            return Fine_Apply(request)
        else:
            print("ERROR FROM INVALID")
    return render(request, 'FineSystemapp/Add_Rules.html', {'form': form})

