# Generated by Django 3.2.3 on 2021-09-14 21:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='content2',
        ),
        migrations.AddField(
            model_name='post',
            name='content1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
