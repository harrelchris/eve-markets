from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Token",
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
                ("character_id", models.IntegerField()),
                ("character_name", models.CharField(max_length=256)),
                ("access_token", models.CharField(max_length=8192)),
                ("expiration", models.DateTimeField()),
                ("refresh_token", models.CharField(max_length=64)),
            ],
        ),
    ]
