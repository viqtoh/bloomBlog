# Generated by Django 3.2.3 on 2021-07-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='html',
            field=models.TextField(default=models.TextField()),
        ),
    ]
