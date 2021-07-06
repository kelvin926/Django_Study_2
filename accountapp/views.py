from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from accountapp.models import HelloWorld
from django.urls import reverse

# Create your views here.

def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("hello_world_input")
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
