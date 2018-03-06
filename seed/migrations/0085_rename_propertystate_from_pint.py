# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-11 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0084_copy_propertystate_orig_pint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertystate',
            old_name='conditioned_floor_area_pint',
            new_name='conditioned_floor_area',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='gross_floor_area_pint',
            new_name='gross_floor_area',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='occupied_floor_area_pint',
            new_name='occupied_floor_area',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='site_eui_pint',
            new_name='site_eui',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='site_eui_modeled_pint',
            new_name='site_eui_modeled',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='site_eui_weather_normalized_pint',
            new_name='site_eui_weather_normalized',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='source_eui_modeled_pint',
            new_name='source_eui_modeled',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='source_eui_pint',
            new_name='source_eui',
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='source_eui_weather_normalized_pint',
            new_name='source_eui_weather_normalized',
        ),
    ]
