# Generated by Django 3.0.8 on 2020-07-15 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200712_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date']},
        ),
    ]
