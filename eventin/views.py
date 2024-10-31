from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Event, Participant, Register
from .serializers import (
    EventSerializer,
    ParticipantSerializer,
    RegisterSerializer,
    GetRegistersByEventSerializer,
    GetRegistersByParticipantSerializer
)

class EventViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class GetRegistersByParticipant(generics.ListAPIView):
    serializer_class = GetRegistersByParticipantSerializer

    def get_queryset(self):
        participant_id = self.kwargs['pk']
        return Register.objects.filter(participant_id=participant_id)


class GetRegisterByEvent(generics.ListAPIView):
    serializer_class = GetRegistersByEventSerializer

    def get_queryset(self):
        event_id = self.kwargs['pk']
        return Register.objects.filter(event_id=event_id)


