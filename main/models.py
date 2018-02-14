from django.db import models

class Player(models.Model):
    id = models.AutoField(primary_key=True) #auto?
    name = models.CharField(max_length=200)

class Field(models.Model):
    id = models.AutoField(primary_key=True) #auto?
    name = models.CharField(max_length=200)

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    date_and_time = models.DateField()
    # player1 = models.ForeignKey(Player, on_delete=models.CASCADE) #I think this may be wrong...
    # player2 = models.ForeignKey(Player, on_delete=models.CASCADE) #Many players to many matches
    # player1 = models.CharField(max_length=200)
    # player2 = models.CharField(max_length=200)
    player1 = models.ManyToManyField(Player, related_name="player1")
    player2 = models.ManyToManyField(Player, related_name="player2")
    field = models.ForeignKey(Field, on_delete=models.CASCADE) #what does this mean.. on delete cascade
    result = models.IntegerField() #store the result in a json object...?
