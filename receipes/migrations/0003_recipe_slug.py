# Generated by Django 5.0.2 on 2024-03-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes', '0002_alter_recipe_created_at_alter_recipe_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
