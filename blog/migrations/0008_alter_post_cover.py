# Generated by Django 4.0.3 on 2022-03-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_view_count_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
