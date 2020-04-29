# Generated by Django 2.2.10 on 2020-04-13 23:03

from django.db import migrations, models


def forwards(apps, schema_editor):
    Rule = apps.get_model('seed', 'Rule')
    # Total 1226 rows/rules;
    # ====================================================================================================================================== #
    # data_type is not null (1055) ---> data_type = 1 (171) ---> text_match is null (107) ---> not_null or required?                         #
    #                               |                       |--> test_match not null (64) ---> text_match != '' (63): include                #
    #                               |                                                     |--> text_match = '' (1) --> not_null or required? #
    #                               |                                                                                                        #
    #                               |-> data_type != 1 (884) ---> min and max are null (32) ---> not_null or required?                       #
    #                                                        |--> min or max not null (852): range                                           #
    #                                                                                                                                        #
    # data_type is null (171) --------> min and max are null (170) ---> text_match is null (170) ---> not_null or required?                  #
    #                         |                                    |--> text_match not null (0) ----> include                                #
    #                         |-------> min or max not null (1) ---> range                                                                   #
    # ====================================================================================================================================== #
    Rule.objects.filter(data_type=1, text_match=None, not_null=True).update(condition='not_null') # TODO: ?
    Rule.objects.filter(data_type=1, text_match=None, required=True, not_null=False).update(condition='required')
    Rule.objects.filter(data_type=1, text_match=None, required=False, not_null=False).update(condition='')
    Rule.objects.filter(data_type=1, text_match='').filter(not_null=True).update(condition='not_null') # TODO: ?
    Rule.objects.filter(data_type=1, text_match='').filter(required=True, not_null=False).update(condition='required')
    Rule.objects.filter(data_type=1, text_match='').filter(required=False, not_null=False).update(condition='')
    Rule.objects.filter(data_type=1).exclude(text_match=None).exclude(text_match='').update(condition='include')

    Rule.objects.exclude(data_type=1).filter(min=None, max=None, not_null=True).update(condition='not_null') # TODO: ?
    Rule.objects.exclude(data_type=1).filter(min=None, max=None, required=True, not_null=False).update(condition='required')
    Rule.objects.exclude(data_type=1).filter(min=None, max=None, required=False, not_null=False).update(condition='')
    Rule.objects.exclude(data_type=1, min=None, max=None).update(condition='range')

    Rule.objects.filter(data_type=None, min=None, max=None, text_match=None, not_null=True).update(condition='not_null')
    Rule.objects.filter(data_type=None, min=None, max=None, text_match=None, required=True, not_null=False).update(condition='required')
    Rule.objects.filter(data_type=None, min=None, max=None, text_match=None, required=False, not_null=False).update(condition='')
    Rule.objects.filter(data_type=None, min=None, max=None).exclude(text_match=None).update(condition='include')
    Rule.objects.filter(data_type=None).exclude(min=None, max=None).update(condition='range')


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0124_auto_20200323_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='condition',
            field=models.CharField(blank=True, default='', max_length=200),
        ),

        migrations.RunPython(forwards),
    ]
