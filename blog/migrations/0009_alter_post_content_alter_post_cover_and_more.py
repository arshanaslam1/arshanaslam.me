# Generated by Django 4.0.3 on 2022-03-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='users/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.CharField(help_text='Keywords separate by comma.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_description',
            field=models.TextField(null=True),
        ),
    ]