from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meetings


#def welcome(request):
   # return HttpResponse("Welcome to the Meeting Planner 3!")

#def welcome(request):
#    return render(request, "website/welcome.html", { "message1": " Does this data really come from view inside"})
 

def welcome(request):
    return render(request, "website/welcome.html",{"num_meetings": Meetings.objects.count() })

def welcome2(request):
    return HttpResponse("Welcome to the Meeting Planner 3 in VS!")

def about(request):
    return render(request,"website/about.html", {"message2": "about message from view_message2"})

#def about(request):
 #   return HttpResponse("About Us Page")

