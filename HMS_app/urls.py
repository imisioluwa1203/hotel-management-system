from django.urls import path
from . import views

urlpatterns = [
  path('',views.dashboard, name = 'dashboard'),
  path('roomsmanagement/',views.RoomsManagement, name = 'ManageRooms'),
  path('addroom/',views.AddRoom, name='AddRoom'),
  path('guestinfo/', views.GuestInfo,name='GuestInfo'),
  path('roomstatus/', views.RoomStatus, name='RoomStatus'),
]