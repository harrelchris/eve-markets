from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alliance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creator_corporation_id", models.IntegerField()),
                ("creator_id", models.IntegerField()),
                ("date_founded", models.CharField(max_length=256)),
                ("executor_corporation_id", models.IntegerField(null=True)),
                ("faction_id", models.IntegerField(null=True)),
                ("name", models.CharField(max_length=256)),
                ("ticker", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("alliance_id", models.IntegerField(null=True)),
                ("birthday", models.CharField(max_length=256)),
                ("bloodline_id", models.IntegerField()),
                ("corporation_id", models.IntegerField()),
                ("description", models.TextField(null=True)),
                ("faction_id", models.IntegerField(null=True)),
                ("gender", models.CharField(max_length=8)),
                ("name", models.CharField(max_length=256)),
                ("race_id", models.IntegerField()),
                ("security_status", models.FloatField(null=True)),
                ("title", models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Corporation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("alliance_id", models.IntegerField(null=True)),
                ("ceo_id", models.IntegerField()),
                ("creator_id", models.IntegerField()),
                ("date_founded", models.CharField(max_length=256)),
                ("description", models.TextField(null=True)),
                ("faction_id", models.IntegerField(null=True)),
                ("home_station_id", models.IntegerField(null=True)),
                ("member_count", models.IntegerField()),
                ("name", models.CharField(max_length=256)),
                ("shares", models.BigIntegerField()),
                ("tax_rate", models.FloatField()),
                ("ticker", models.CharField(max_length=256)),
                ("url", models.CharField(max_length=256, null=True)),
                ("war_eligible", models.BooleanField()),
            ],
        ),
    ]
