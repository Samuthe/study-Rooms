from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'lets learn javascript'},
    {'id': 3, 'name': 'lets learn django'},
    {'id': 4, 'name': 'lets learn data science'},
    {'id': 5, 'name': 'lets learn LLM'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
    #return render(request, 'home.html', {'rooms': rooms})
    # return HttpResponse('Home page')

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
            break
    context = {'room': room}
    return render(request, 'base/room.html', context)
    # return HttpResponse('Rooms')
