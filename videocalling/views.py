from django.http import HttpResponse
from django.shortcuts import render


def video_calling(request):
    return render(request,'video_calling.html')