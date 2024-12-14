# Generated by Django 5.1.4 on 2024-12-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(choices=[('Football', 'Football'), ('Boxing', 'Boxing'), ('Running', 'Running'), ('Team_games', 'Team games'), ('Tennis', 'Tennis'), ('F1', 'Formula-1'), ('Olympic_games', 'Olympic games'), ('Winter_sports', 'Winter sports'), ('Fitness', 'Fitness'), ('Extreme_sports', 'Extreme sports'), ('Top_athletes', 'Top athletes')], max_length=15, unique=True),
        ),
    ]
