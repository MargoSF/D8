# Generated by Django 4.2 on 2023-07-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='choice',
            field=models.CharField(choices=[('posts', 'Новости'), ('articles', 'Статьи')], default='articles', max_length=10),
        ),
    ]