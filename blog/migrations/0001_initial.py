# Generated by Django 4.2.11 on 2024-04-28 17:25

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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('restaurant_name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('visited_on', models.DateTimeField()),
                ('rating', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
