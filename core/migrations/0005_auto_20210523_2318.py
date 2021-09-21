# Generated by Django 3.2.3 on 2021-05-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_approved_post_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Tecnologia'), ('CR', 'Curiosidades'), ('GR', 'Geral')], default='GR', max_length=4),
        ),
    ]