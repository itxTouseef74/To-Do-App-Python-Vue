from django.shortcuts import HttpResponse

def home(  request):
        return HttpResponse("WELCOME TO TODO APP API")
