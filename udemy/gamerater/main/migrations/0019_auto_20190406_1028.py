# Generated by Django 2.1.7 on 2019-04-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20190406_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='info',
        ),
        migrations.AddField(
            model_name='game',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(1, 'Survival-Horror'), (3, 'Survival'), (0, 'Sci-Fi'), (4, 'Race'), (2, 'Horror')], default=0),
        ),
    ]
