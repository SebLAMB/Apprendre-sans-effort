# Generated by Django 2.2.5 on 2019-11-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0031_auto_20191115_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass_DynMCQTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_test', models.CharField(max_length=10, null=True)),
                ('id_student', models.CharField(max_length=10)),
                ('q_num', models.CharField(max_length=10, null=True)),
                ('r_ans', models.TextField()),
            ],
            options={
                'unique_together': {('id_test', 'id_student', 'q_num')},
            },
        ),
    ]