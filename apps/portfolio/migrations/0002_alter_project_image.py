# Generated by Django 4.2.1 on 2023-05-09 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='media/postfolio/images/'),
        ),
    ]
