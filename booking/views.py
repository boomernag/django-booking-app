from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """

    return render (request, 'booking/index.html')


def make_a_booking(request):
    """ A view to choose day and time for booking """

    return render (request, 'booking/make_a_booking.html')


def book(request):
    """ A view as confirmation of a booking """

    return render (request, 'booking/index.html')