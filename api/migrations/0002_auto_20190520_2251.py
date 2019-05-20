# Generated by Django 2.2.1 on 2019-05-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]