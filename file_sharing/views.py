
from django.shortcuts import render


def files(request):
    return render(request,'files.html')