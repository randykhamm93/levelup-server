from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=55)
    organizer = models.ForeignKey(
        'Gamer', on_delete=models.CASCADE, related_name="organized_events")
    game = models.ForeignKey(
        'Game', on_delete=models.CASCADE, related_name="events")
    date_time = models.DateTimeField()
    location = models.CharField(max_length=55)
    maker = models.CharField(max_length=25)
    number_of_players = models.IntegerField(default=0)
    skill_level = models.CharField(max_length=20)
