# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

# Create your views here.
from dash.models import Profile, Education_and_Experience, Project


def home(request):
    profile = Profile.objects.all()
    if(profile.count() == 0):
        return render(request, "set_db.html")
    else:
        profile = Profile.objects.all()[0]
    context={
        'active':'home',
        "profile":profile
    }
    return render(request, "index.html", context)


def about(request):
    profile = Profile.objects.all()
    if(profile.count() == 0):
        return render(request, "set_db.html")
    else:
        profile = Profile.objects.all()[0]
    education_and_work = Education_and_Experience.objects.all()
    context={
        'active':'about',
        "profile":profile,
        "education_and_work":education_and_work
    }
    return render(request, "about.html", context)


def work(request):
    profile = Profile.objects.all()
    if(profile.count() == 0):
        return render(request, "set_db.html")
    else:
        profile = Profile.objects.all()[0]
    project = Project.objects.all()
    context={
        'active':'work',
        'projects':project
    }
    return render(request, "work.html", context)


def contact(request):
    profile = Profile.objects.all()
    if(profile.count() == 0):
        return render(request, "set_db.html")
    else:
        profile = Profile.objects.all()[0]
    context={
        'active':'contact',
        "profile":profile
    }
    return render(request, "contact.html", context)
