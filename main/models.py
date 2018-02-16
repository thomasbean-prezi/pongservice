from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Field(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    date_and_time = models.DateField()
    player1 = models.ForeignKey(Player, related_name="player1")
    player2 = models.ForeignKey(Player, related_name="player2")
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    field = models.ForeignKey(Field, related_name="field")
