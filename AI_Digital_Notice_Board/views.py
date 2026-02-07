from django.shortcuts import render
from apps.notice.models import Notice

def about(request):
    return render(request, "about.html")

def home(request):
    notices = Notice.objects.all()
    return render(request, "home.html", {"notices": notices})
