# Generated by Django 3.1.7 on 2021-03-16 10:28

from django.db import migrations
import esite.colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0005_auto_20210316_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='color',
            field=esite.colorfield.fields.ColorField(help_text='Select color that fitd your mood.', max_length=18),
        ),
    ]
