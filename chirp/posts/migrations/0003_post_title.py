# Generated by Django 4.0.5 on 2022-07-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_post_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Default Title', max_length=100),
            preserve_default=False,
        ),
    ]