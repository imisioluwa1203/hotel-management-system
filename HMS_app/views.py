from django.shortcuts import render
from django.template.context_processors import request
from .models import RoomStatus
from .models import RoomCategory
from django.contrib import messages #import messages
from django.shortcuts import render, redirect,get_object_or_404


# Create your views here.


def dashboard(request):
  return render(request,'dashboard.html')


def RoomsManagement(request):
  return render(request,'ManageRooms.html')

def AddRoom(request):
  categoriess = RoomCategory.objects.all()
  Statusess = RoomStatus.objects.all()

  return render(request, 'addRoom.html', {'categoriess':categoriess, 'Statusess':Statusess})


def GuestInfo(request):
  return render(request,'guestInfo.html')


def RoomStatusView(request):
  if request.method == 'POST':
    roomstatus = request.POST.get('roomstatus')
    
    if roomstatus:
      RoomStatus.objects.create(status=roomstatus)
      messages.success(request,'Room status submitted succesfully') #ADD messge success
    else:
      messages.error(request,'please enter a room status')
      #Getting all rooms to show in the table
  all_table = RoomStatus.objects.all()

  return render(request,'roomstatus.html',{'statuses':all_table})

def update_Room_Status(request, id):
    try:
        status = RoomStatus.objects.get(id=id)
    except RoomStatus.DoesNotExist:
        messages.error(request, 'Room status not found.')
        return redirect('roomstatus')

    if request.method == 'POST':
        new_status = request.POST.get('roomstatus')
        if new_status:
            status.status = new_status
            status.save()
            messages.success(request, 'Room status updated successfully.')
            return redirect('roomstatus')
        else:
            messages.error(request, 'Please enter a valid room status.')

    return render(request, 'updateroomstatus.html', {'status': status})


def delete_Room_Status(request,id):
   status_obj = get_object_or_404(RoomStatus, id =id)
   status_obj.delete()
   messages.success(request,'Room stsatus deleted successfully')
   return redirect('roomstatus')




def room_Category(request):
   
 if request.method == 'POST':
      roomcategory = request.POST.get('roomcategory')

      if roomcategory:
         RoomCategory.objects.create(Category=roomcategory)
         messages.success(request,'Room Catogry submitted succesfully') #ADD messge success
      else:
          messages.error(request,'please enter a room category')
              #Getting all rooms to show in the table
 all_tablee = RoomCategory.objects.all()

 return render(request,'roomCategory.html',{'Categories':all_tablee})


def Update_room_category(request,id):   # Define function for the update of room category!

  # Error handling incase room category entered not in the list! 
  try:
     Category = RoomCategory.objects.get(id=id) 
  except RoomCategory.DoesNotExist:
     
     # Success & Error incase the data are subbmitted or Not
     messages.error(request, 'Room status not Found!.')
     return redirect('roomcategory')
  
  # Check if the request is a Post 
  if request.method == 'POST':
     new_category = request.POST.get('roomcategory')

   # To update the new category if new one is entered.....
     if new_category:
        Category.Category = new_category

        # Save the new categorry updated...
        Category.save()

        #Then another Success & Error message....
        messages.success(request, ' Room Categories Succesfully updated!!!')
        return redirect('roomCategory')
     else:
        messages.error(request, 'Please enter a valid Room Status')

  return render(request, 'updateroomcategory.html',{'Category':Category})
   
def delete_room_category(request, id): #Define the function.  "To delete the request made through the id"
    category_obj = get_object_or_404(RoomCategory, id = id)
    category_obj.delete()
    messages.success(request,'Room stsatus deleted successfully')
    return redirect('roomCategory')
