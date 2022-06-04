from django.shortcuts import render
from .models import Clas, Club, Reservation
# this should be temporary
from django.http import HttpResponse
# naah
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

# get salles and display the unreserved ones
def index(request):
    claslis = Clas.objects.all()
    class_list = []
    for c in claslis:
        if not hasattr(c, 'reservation'):
            class_list += [c]
    context = {'class_list': class_list}
    return render(request, 'classroomgmt/index.html', context)

@login_required(login_url='/login/')
def book(request, class_id):
    user = request.user
    # if staff dont let it pass.. staff shouldnt be reserving from here they
    # have no club lol
    if user.is_staff:
        return render(request, 'classroomgmt/failedtobook.html', {})
    try:
        clas = Clas.objects.get(pk=class_id)
        club = user.club
    except Clas.DoesNotExist:
        raise Http404('Class does not exist')
    context = {
        'class_name': clas.name,
    }
    reservation = Reservation.objects.create(clas=clas, club=club)
    clas.save()
    reservation.save()

    return render(request, 'classroomgmt/booked.html', context) 

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('classroomgmt:index'))



#done i guess
