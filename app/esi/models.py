from django.db import models


class Alliance(models.Model):
    creator_corporation_id = models.IntegerField()
    creator_id = models.IntegerField()
    date_founded = models.CharField(max_length=256)  # TODO: should be datetime
    executor_corporation_id = models.IntegerField(null=True)
    faction_id = models.IntegerField(null=True)
    name = models.CharField(max_length=256)
    ticker = models.CharField(max_length=256)


class Character(models.Model):
    alliance_id = models.IntegerField(null=True)
    birthday = models.CharField(max_length=256)  # TODO: should be datetime
    bloodline_id = models.IntegerField()
    corporation_id = models.IntegerField()
    description = models.TextField(null=True)
    faction_id = models.IntegerField(null=True)
    gender = models.CharField(max_length=8)
    name = models.CharField(max_length=256)
    race_id = models.IntegerField()
    security_status = models.FloatField(null=True)
    title = models.CharField(max_length=256, null=True)


class Corporation(models.Model):
    alliance_id = models.IntegerField(null=True)
    ceo_id = models.IntegerField()
    creator_id = models.IntegerField()
    date_founded = models.CharField(max_length=256)  # TODO: should be datetime
    description = models.TextField(null=True)
    faction_id = models.IntegerField(null=True)
    home_station_id = models.IntegerField(null=True)
    member_count = models.IntegerField()
    name = models.CharField(max_length=256)
    shares = models.BigIntegerField()
    tax_rate = models.FloatField()
    ticker = models.CharField(max_length=256)
    url = models.CharField(max_length=256, null=True)
    war_eligible = models.BooleanField()
