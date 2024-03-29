# Generated by Django 4.0.2 on 2023-05-19 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('biography', models.TextField(blank=True)),
                ('profile_img', models.ImageField(default='blank pic.png', upload_to='profile_images')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('follower', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
