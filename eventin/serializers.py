from rest_framework import serializers
from .models import Event, Participant, Registert

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
        model = Registert
        fields = ['id', 'event', 'participant', 'date_event']

