from rest_framework import serializers
from .models import Event, Participant, Register

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'local',
            'date_event',
            'capacity'
        ]


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'cpf', 'email', 'phone']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'event', 'participant', 'date_register']

