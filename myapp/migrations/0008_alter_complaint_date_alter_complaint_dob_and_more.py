# Generated by Django 4.0.2 on 2022-04-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_complaint_date_alter_fir_sdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='idate',
            field=models.DateField(null=True),
        ),
    ]
