# Generated by Django 3.1.12 on 2024-12-13 07:25

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20241213_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizuser',
            name='id',
            field=models.CharField(default=quiz.models.generate_object_id, max_length=24, primary_key=True, serialize=False),
        ),
    ]
