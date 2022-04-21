# Generated by Django 4.0.3 on 2022-04-21 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='Food', to='recipes.fooditem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measurement',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, related_name='measurement', to='recipes.measure'),
            preserve_default=False,
        ),
    ]
