# Generated by Django 2.1.5 on 2020-07-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0008_auto_20200701_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopimage',
            old_name='shop_image',
            new_name='shopimage',
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='shop_image',
            field=models.FileField(null=True, upload_to='shops/', verbose_name=''),
        ),
    ]
