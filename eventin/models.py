from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    local = models.CharField(max_length=100)
    date_event = models.DateTimeField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
