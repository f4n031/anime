from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'anime/index.html')

def adm(request):
    return render(request, 'anime/adm.html')
