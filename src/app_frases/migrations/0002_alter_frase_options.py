# Generated by Django 5.2 on 2025-04-29 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_frases', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frase',
            options={'ordering': ['fecha_frase']},
        ),
    ]
