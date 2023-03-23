# Generated by Django 4.1.7 on 2023-03-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]