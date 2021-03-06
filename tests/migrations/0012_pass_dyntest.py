# Generated by Django 2.2.5 on 2019-11-02 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0011_dyntest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass_DynTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_test', models.CharField(max_length=10)),
                ('id_student', models.CharField(max_length=10)),
                ('q_num', models.IntegerField()),
                ('r_text', models.TextField()),
            ],
            options={
                'unique_together': {('id_test', 'id_student', 'q_num')},
            },
        ),
    ]
