from django.shortcuts import render
from .models import Job

from django.shortcuts import HttpResponse


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})