# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-18 23:02
from __future__ import unicode_literals

from django.db import migrations
import quantityfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0071_auto_20170721_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertystate',
            name='conditioned_floor_area_si',
            field=quantityfield.fields.QuantityField(base_units='m**2', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertystate',
            name='gross_floor_area_si',
            field=quantityfield.fields.QuantityField(base_units='m**2', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertystate',
            name='occupied_floor_area_si',
            field=quantityfield.fields.QuantityField(base_units='m**2', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertystate',
            name='site_eui_si',
            field=quantityfield.fields.QuantityField(base_units='GJ/m**2/year', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertystate',
            name='site_eui_weather_normalized_si',
            field=quantityfield.fields.QuantityField(base_units='GJ/m**2/year', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertystate',
            name='source_eui_si',
            field=quantityfield.fields.QuantityField(base_units='GJ/m**2/year', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertystate',
            name='source_eui_weather_normalized_si',
            field=quantityfield.fields.QuantityField(base_units='GJ/m**2/year', blank=True, null=True),
        ),
    ]