# Generated by Django 3.0.4 on 2020-05-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_recipe_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='made_by',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]
