# Generated by Django 4.0.3 on 2022-04-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0027_rename_summery_resume_summary_alter_portfolio_mob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='summary',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='subtitle',
            new_name='organization',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='end',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='start',
        ),
        migrations.AddField(
            model_name='resume',
            name='expirationDate',
            field=models.DateField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='issueDate',
            field=models.DateField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='category',
            field=models.CharField(blank=True, choices=[('Skills', 'Skills'), ('Knowledge', 'Knowledge'), ('Language', 'Language')], max_length=10, null=True),
        ),
    ]