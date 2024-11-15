# Generated by Django 5.1.1 on 2024-10-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
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
                ("title", models.CharField(max_length=200)),
                ("release_date", models.DateField()),
                ("cover_image", models.ImageField(upload_to="albums/")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="BandMember",
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
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("bio", models.TextField()),
                ("image", models.ImageField(upload_to="members/")),
            ],
        ),
        migrations.CreateModel(
            name="Concert",
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
                ("date", models.DateField()),
                ("location", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
    ]
