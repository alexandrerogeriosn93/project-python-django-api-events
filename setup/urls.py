from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from eventin.views import EventViewSet, ParticipantViewSet

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='Events')
router.register('participants', ParticipantViewSet, basename='Participants')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
