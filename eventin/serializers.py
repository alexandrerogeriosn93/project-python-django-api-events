from rest_framework import serializers
from .models import Event, Participant, Register
from .validators import (
    is_invalid_email,
    is_invalid_name, 
    is_invalid_phone,
    is_invalid_cpf
)

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
    
    def validate(self, data):
        if is_invalid_name(data.get('name', '')):
            raise serializers.ValidationError({'name': 'O nome deve conter acima de três caracteres e apenas letras.'})
        
        if is_invalid_email(data.get('email', '')):
            raise serializers.ValidationError({'email': 'O e-mail deve ser válido.'})
        
        if is_invalid_phone(data.get('phone', '')):
            raise serializers.ValidationError({'phone': 'Número de telefone inválido.'})
        
        if is_invalid_cpf(data.get('cpf', '')):
            raise serializers.ValidationError({'cpf': 'Número de CPF inválido.'})
        
        return data


class ParticipantSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'email', 'phone']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'event', 'participant', 'date_register']


class GetRegistersByParticipantSerializer(serializers.ModelSerializer):
    event = serializers.ReadOnlyField(source='event.title')

    class Meta:
        model = Register
        fields = ['event', 'date_register']


class GetRegistersByEventSerializer(serializers.ModelSerializer):
    participant = serializers.ReadOnlyField(source='participant.name')

    class Meta:
        model = Register
        fields = ['participant', 'date_register']


