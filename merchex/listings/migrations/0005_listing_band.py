# Generated by Django 4.2.5 on 2023-09-09 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0004_listing_description_listing_sold_listing_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="band",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="listings.band",
            ),
        ),
    ]
