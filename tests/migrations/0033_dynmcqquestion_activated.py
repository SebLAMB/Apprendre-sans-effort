# Generated by Django 2.2.5 on 2019-11-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0032_pass_dynmcqtest'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynmcqquestion',
            name='activated',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
