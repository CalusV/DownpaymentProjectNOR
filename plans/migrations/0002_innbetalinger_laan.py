# Generated by Django 2.1.2 on 2019-10-22 20:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='innbetalinger',
            name='laan',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='plans.Laan'),
            preserve_default=False,
        ),
    ]
