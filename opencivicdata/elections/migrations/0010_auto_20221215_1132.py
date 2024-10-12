# Generated by Django 3.2.8 on 2022-12-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elections", "0009_auto_20221208_1041"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ballotmeasurecontest",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="The date and time of the last update."
            ),
        ),
        migrations.AlterField(
            model_name="candidacy",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="The date and time of the last update."
            ),
        ),
        migrations.AlterField(
            model_name="candidatecontest",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="The date and time of the last update."
            ),
        ),
        migrations.AlterField(
            model_name="election",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="The date and time of the last update."
            ),
        ),
        migrations.AlterField(
            model_name="partycontest",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="The date and time of the last update."
            ),
        ),
        migrations.AlterField(
            model_name="retentioncontest",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="The date and time of the last update."
            ),
        ),
    ]
