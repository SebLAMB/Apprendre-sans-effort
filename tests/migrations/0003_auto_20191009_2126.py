# Generated by Django 2.2.5 on 2019-10-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_remove_choice_is_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_mcq_end_session',
            name='answer_num_exp',
            field=models.TextField(),
        ),
    ]
