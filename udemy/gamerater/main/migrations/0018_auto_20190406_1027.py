# Generated by Django 2.1.7 on 2019-04-06 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_delete_extrainfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.IntegerField(choices=[(3, 'Survival'), (1, 'Survival-Horror'), (0, 'Sci-Fi'), (2, 'Horror'), (4, 'Race')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='id',
        ),
        migrations.AddField(
            model_name='game',
            name='info',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.ExtraInfo'),
            preserve_default=False,
        ),
    ]
