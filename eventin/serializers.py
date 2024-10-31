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

    def validate_name(self, name):
        if not name.replace(' ', '').isalpha():
            raise serializers.ValidationError('O nome deve contar letras e espaços.')
        
        if not len(name) >= 3:
            raise serializers.ValidationError('O nome deve conter mais de três caracteres.')
        
        return name
    
    def validate_email(self, email):
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise serializers.ValidationError('O e-mail deve ser válido.')
        
        return email
    
    def validate_phone(self, phone):
        if len(phone) < 11 or not phone.isdigit():
            raise serializers.ValidationError('O telefone deve conter onze dígitos.')
        
        return phone


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


