# Generated by Django 2.1a1 on 2018-11-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculateResults', '0011_auto_20181028_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=111814),
            preserve_default=False,
        ),
    ]
