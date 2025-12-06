from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.
def dashboard(request):
  return render(request,'dashboard.html')


def RoomsManagement(request):
  return render(request,'ManageRooms.html')

def AddRoom(request):
  return render(request, 'addRoom.html')


def GuestInfo(request):
  return render(request,'guestInfo.html')


def RoomStatus(request):
  return render(request,'roomStatus.html')