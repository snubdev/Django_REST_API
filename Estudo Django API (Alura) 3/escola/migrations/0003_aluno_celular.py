# Generated by Django 3.2.18 on 2023-03-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
    ]
