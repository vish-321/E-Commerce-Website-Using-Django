# Generated by Django 3.0.9 on 2020-08-09 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category_belongs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.Category'),
            preserve_default=False,
        ),
    ]
