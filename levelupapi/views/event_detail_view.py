from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from levelupapi.models import Event
from .event_view import EventSerializer

class EventDetailView(APIView):
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        organizer_first_name = event.organizer.user.first_name
        organizer_last_name = event.organizer.user.last_name
        event_data = EventSerializer(event).data
        event_data['organizer_first_name'] = organizer_first_name
        event_data['organizer_last_name'] = organizer_last_name
        return Response(event_data)
