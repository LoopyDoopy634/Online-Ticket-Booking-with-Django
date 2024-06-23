from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Ticket
from .forms import TicketForm
from django.contrib import messages

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, event=event)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event
            ticket.save()
            messages.success(request, 'Ticket booked successfully!')
            form = TicketForm(event=event)  # Clear the form
    else:
        form = TicketForm(event=event)
    return render(request, 'book_ticket.html', {'form': form, 'event': event})

def event_bookings(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    tickets = Ticket.objects.filter(event=event)
    return render(request, 'event_bookings.html', {'event': event, 'tickets': tickets})

