# Generated by Django 3.0.14 on 2022-04-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
