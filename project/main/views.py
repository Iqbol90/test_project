from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def basic(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def packages(request):
    return render(request, 'main/packages.html')


def pricing(request):
    return render(request, 'main/pricing.html')

