# Generated by Django 3.1.12 on 2024-12-13 06:44

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20241213_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizuser',
            name='id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
