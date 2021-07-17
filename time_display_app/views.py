from django.shortcuts import render, HttpResponse
from time import localtime, strftime, gmtime

def index(request):
    context = {
        "day": strftime('%A %B %d', gmtime()),
        "time": strftime('%H:%M %p %z', localtime()),
    }
    return render(request, 'index.html', context)


