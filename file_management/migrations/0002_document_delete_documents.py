# Generated by Django 5.1.1 on 2024-09-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
    ]
