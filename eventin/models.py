from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

class Event(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    description = models.TextField(validators=[MinLengthValidator(10)])
    local = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    date_event = models.DateTimeField()
    capacity = models.PositiveIntegerField(validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    email = models.EmailField(max_length=100, validators=[EmailValidator()])
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
    

class Register(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registers')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='registers')
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.participant.name} inscrito em: {self.event.title}'


