# Generated by Django 4.2.9 on 2024-01-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
