from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from eventin.views import (
    EventViewSet,
    ParticipantViewSet,
    RegisterViewSet,
    GetRegisterByEvent,
    GetRegistersByParticipant
)

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='Events')
router.register('participants', ParticipantViewSet, basename='Participants')
router.register('registers', RegisterViewSet, basename='Registers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('participants/<int:pk>/registers', GetRegistersByParticipant.as_view()),
    path('events/<int:pk>/registers', GetRegisterByEvent.as_view())
]
