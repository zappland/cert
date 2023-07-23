# Generated by Django 4.2.2 on 2023-07-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='ata',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='ats_w',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='cert_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='comments_from_last_wksh',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='cst',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='cst_subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='current_comment',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='eas',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='expiration_date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='las',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='nys_cert_area',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='subject_grade',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
