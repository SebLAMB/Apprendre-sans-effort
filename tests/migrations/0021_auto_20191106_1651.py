# Generated by Django 2.2.5 on 2019-11-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0020_auto_20191102_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynTestInfo',
            fields=[
                ('id_test', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
                ('nb_q', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='dyntest',
            name='title',
        ),
    ]