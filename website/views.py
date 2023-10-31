from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meetings


#def welcome(request):
   # return HttpResponse("Welcome to the Meeting Planner 3!")

#def welcome(request):
#    return render(request, "website/welcome.html", { "message1": " Does this data really come from view inside"})
 

#def welcome(request):
#    return render(request, "website/welcome.html",{"num_meetings": Meetings.objects.count()})

#def welcome(request):
#    return render (request, "website/welcome.html",{"meetings": Meetings.objects.all()})


#def welcome(request):
 #   return render (request, "website/welcome.html",{"count_meeting": Meetings.objects.count()})


#def welcome(request):
 #   return render (request, "website/welcome.html",{"checks": Meetings.objects.all()})


def welcome(request):
    return render (request, "website/welcome.html",{"meetings":Meetings.objects.all()})

#getting the meeting name
#def welcome(request):
 #   return render(request,"website/welcome.html",{"meeting_title":Meetings.objects.name()})

#def welcome(request):
 #   return render (request, "website/welcome.html",{"count_meetings":Meetings.objects.count()})

#def welcome(request):
 #   return render (request, "website/welcome.html",{"meetings":Meetings.objects.all()})



def welcome2(request):
    return HttpResponse("Welcome to the Meeting Planner 3 in VS!")

def about(request):
    return render(request,"website/about.html", {"message2": "about message from view_message2"})

#def about(request):
 #   return HttpResponse("About Us Page")

