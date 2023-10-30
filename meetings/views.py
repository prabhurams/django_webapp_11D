from django.shortcuts import render

from .models import Meetings

def detail(request,id):
    meeting = Meetings.objects.get(pk=id)
    return render(request,"meetings/details.html", {"meeting":meeting})

# Create your views here.
