from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Ticket.objects.filter(event=self.event, email=email).exists():
            raise forms.ValidationError("You have already booked a ticket for this event with this email.")
        return email
