# Generated by Django 5.0.6 on 2024-06-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curr_ID', models.IntegerField()),
                ('Date', models.DateTimeField()),
                ('Cur_Abbreviation', models.CharField(max_length=3)),
                ('Cur_Scale', models.SmallIntegerField()),
                ('Cur_name', models.CharField(max_length=50)),
                ('Cur_OfficialRate', models.FloatField()),
            ],
            options={
                'verbose_name': 'rate',
                'verbose_name_plural': 'rates',
                'db_table': 'rate',
            },
        ),
    ]
