# Generated by Django 5.0.3 on 2024-06-08 13:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("commentApp2", "0002_rename_content_comment2_comment_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment2",
            old_name="comment",
            new_name="feed",
        ),
    ]
