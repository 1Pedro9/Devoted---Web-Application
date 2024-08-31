# Generated by Django 5.0.6 on 2024-07-30 10:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('plan', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.member')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('journal_id', models.AutoField(primary_key=True, serialize=False)),
                ('journal', models.CharField(default='cuj', max_length=5)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('details', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.category')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.member')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('budget_id', models.AutoField(primary_key=True, serialize=False)),
                ('budget', models.CharField(default='Monthly Budget #1', max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('details', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.category')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.member')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.plan')),
            ],
        ),
    ]
