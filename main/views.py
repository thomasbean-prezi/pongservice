from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

from .models import Player

def index(request):
    players = Player.objects.all()
    # template = loader.get_template('main/index.html')
    context = {
        'players': players, #is this how you pass the 'player' variable to the index?
    }
    return render(request, 'main/index.html', context)
    # return HttpResponse(template.render(context, request))
    #return HttpResponse("woo. you are at the main page. exciting stuff")

# Create your views here.
