from django.db import models


class Game(models.Model):

    title = models.CharField(max_length=55)
    creator = models.ForeignKey(
        'Gamer', on_delete=models.CASCADE, related_name="created_games")
    game_type = models.ForeignKey(
        'GameType', on_delete=models.CASCADE, related_name="games")
    maker = models.CharField(max_length=25)
    number_of_players = models.IntegerField(default=0)
    skill_level = models.CharField(max_length=20)
