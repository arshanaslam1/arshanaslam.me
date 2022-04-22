# Generated by Django 4.0.3 on 2022-04-18 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0017_knowledge_language_remove_skills_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.CharField(blank=True, max_length=32, null=True)),
                ('enddate', models.CharField(blank=True, max_length=32, null=True)),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('summery', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Award',
                'verbose_name_plural': 'Awards',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.CharField(blank=True, max_length=32, null=True)),
                ('enddate', models.CharField(blank=True, max_length=32, null=True)),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('summery', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certificationa',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.CharField(blank=True, max_length=32, null=True)),
                ('enddate', models.CharField(blank=True, max_length=32, null=True)),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('summery', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.CharField(blank=True, max_length=32, null=True)),
                ('enddate', models.CharField(blank=True, max_length=32, null=True)),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('summery', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiencea',
            },
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='ResumeCategory',
        ),
    ]