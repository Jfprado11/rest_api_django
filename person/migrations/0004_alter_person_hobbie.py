# Generated by Django 4.0.7 on 2022-09-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_person_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='hobbie',
            field=models.CharField(max_length=500),
        ),
    ]
