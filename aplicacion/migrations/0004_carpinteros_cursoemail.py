# Generated by Django 4.2.3 on 2023-08-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_delete_electricistas'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpinteros',
            name='cursoemail',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
