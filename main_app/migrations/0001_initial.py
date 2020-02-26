# Generated by Django 2.2 on 2020-02-25 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('difficulty', models.CharField(max_length=255)),
                ('stars', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('completed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed', to='main_app.User')),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trails', to='main_app.User')),
            ],
        ),
    ]
