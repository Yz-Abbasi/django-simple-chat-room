from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse


# Create your views here.
def home(request):

    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)

    return render(request, 'room.html', {
        'username': username,
        'room': 'room',
        'room_details': room_details,
    })


def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room_name).exists():
        return redirect('/' + room_name + '/?username=' + username)

    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect('/' + room_name + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(msg=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse('Message sent successfully')
