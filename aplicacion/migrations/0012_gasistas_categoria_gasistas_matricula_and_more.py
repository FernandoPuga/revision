# Generated by Django 4.2.3 on 2023-08-10 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_electricistas_categoria_electricistas_matricula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasistas',
            name='categoria',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='gasistas',
            name='matricula',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='gasistas',
            name='precio',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='pintores',
            name='precio',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='plomeros',
            name='categoria',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='plomeros',
            name='matricula',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='plomeros',
            name='precio',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='electricistas',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='electricistas',
            name='matricula',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='electricistas',
            name='precio',
            field=models.CharField(max_length=50),
        ),
    ]
