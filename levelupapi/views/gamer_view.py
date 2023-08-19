from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from levelupapi.models import Gamer
from rest_framework.decorators import action

class GamerView(ViewSet):
    """Level up gamer view"""

    def list(self, request):
        """Handle GET requests to get all gamers

        Returns:
            Response -- JSON serialized list of gamers
        """
        gamers = Gamer.objects.all()
        serializer = GamerSerializer(gamers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single gamer

        Returns:
            Response -- JSON serialized gamer
        """
        gamer = Gamer.objects.get(pk=pk)
        serializer = GamerSerializer(gamer)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            try:
                gamer = Gamer.objects.get(user__id=user_id)
                serializer = GamerSerializer(gamer)
                return Response(serializer.data)
            except Gamer.DoesNotExist:
                return Response({'error': 'Gamer not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'user_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for gamers
    """
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Gamer
        fields = ('id', 'user', 'bio', 'events', 'first_name', 'last_name')

