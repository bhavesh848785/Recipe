# Generated by Django 5.0.2 on 2024-03-19 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_menu_updated_at'),
        ('receipes', '0007_alter_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='breakfast',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='break_fast', to='receipes.recipe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='dinner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dinner', to='receipes.recipe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='lunch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lunch', to='receipes.recipe'),
            preserve_default=False,
        ),
    ]
