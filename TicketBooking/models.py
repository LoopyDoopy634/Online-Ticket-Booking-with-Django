from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.event.name}"
