from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Event, Participant, Register
from .serializers import (
    EventSerializer,
    ParticipantSerializer,
    ParticipantSerializerV2,
    RegisterSerializer,
    GetRegistersByEventSerializer,
    GetRegistersByParticipantSerializer
)
from django_filters.rest_framework import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title']


class ParticipantViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Participant.objects.all()
    # serializer_class = ParticipantSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ParticipantSerializerV2
        return ParticipantSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date_register']
    search_fields = ['date_register']


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


