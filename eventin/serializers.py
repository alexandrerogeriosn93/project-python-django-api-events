from rest_framework import serializers
from .models import Event, Participant

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


