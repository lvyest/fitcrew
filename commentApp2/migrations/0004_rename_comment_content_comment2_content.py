# Generated by Django 5.0.3 on 2024-06-08 13:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("commentApp2", "0003_rename_comment_comment2_feed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment2",
            old_name="comment_content",
            new_name="content",
        ),
    ]
