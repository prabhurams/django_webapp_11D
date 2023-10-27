from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner 3!")

def welcome2(request):
    return HttpResponse("Welcome to the Meeting Planner 3 in VS!")

def about(request):
    return HttpResponse("About Us Page")
