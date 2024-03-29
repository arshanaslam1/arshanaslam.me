# Generated by Django 4.0.3 on 2022-04-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0030_contact_user_alter_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='category',
            field=models.CharField(choices=[('Education', 'Education'), ('Experience', 'Experience'), ('Certification', 'Certification'), ('Awards', 'Awards')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='issueDate',
            field=models.DateField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='organization',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='category',
            field=models.CharField(choices=[('Skills', 'Skills'), ('Knowledge', 'Knowledge'), ('Language', 'Language')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='percentage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='title',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
