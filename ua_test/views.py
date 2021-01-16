from django.shortcuts import render


def index(request):
    return render(request, 'ua_test/index.html')
