# Generated by Django 3.2 on 2021-04-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repository',
            field=models.URLField(blank=True, null=True),
        ),
    ]
