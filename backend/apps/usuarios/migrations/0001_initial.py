# Generated by Django 5.2 on 2025-05-14 22:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Perfil",
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
                ("nome_completo", models.CharField(max_length=255)),
                (
                    "nome_social",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("telefone", models.CharField(max_length=20)),
                ("cpf_cnpj", models.CharField(max_length=20)),
                ("endereco", models.CharField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="perfil",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
