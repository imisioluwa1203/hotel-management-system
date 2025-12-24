from django.urls import path
from . import views

urlpatterns = [
  path('',views.dashboard, name = 'dashboard'),
  path('roomsmanagement/',views.RoomsManagement, name = 'ManageRooms'),
  path('addroom/',views.AddRoom, name='AddRoom'),
  path('guestinfo/', views.GuestInfo,name='GuestInfo'),
  path('roomstatus/', views.RoomStatusView, name='roomstatus'),
  path('updateroomstatus/update/<int:id>/', views.update_Room_Status, name='update_room_status'),
  path('deleteroomstatus/delete/<int:id>/', views.delete_Room_Status, name='delete_room_status'),
  path('roomCategory/', views.room_Category, name = 'roomCategory'),
  path('updateroomcategory/update/<int:id>/', views.Update_room_category, name='update_room_category'),
  path('deleteroomcategory/delete/<int:id>/', views.delete_room_category, name='delete_room_category'),

]