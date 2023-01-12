from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'base.html')
  

def index(request):
    return render(request, 'index.html')

def extendsone(request):
    return render(request, 'extendsone.html')







# This is where the real pages begin from    

def about(request):
    return render(request,'about.html')


def form(request):
    return render(request,'form.html')


def payment(request):
    return render(request, 'payment.html')


def knowourteam(request):
    return render(request,'knowourteam.html')