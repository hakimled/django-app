from django.shortcuts import render
import socket



def home(request):
    
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    context = {'ip': ip}
    
    
    return render(request, 'polls/polls.html' , context)