# Generated by Django 2.2.8 on 2020-02-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_meaow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
