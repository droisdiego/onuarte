# Generated by Django 5.0 on 2023-12-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artes', '0012_alter_usuarioperfil_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioperfil',
            name='icone',
            field=models.ImageField(blank=True, default='abstract-user-flat-3.png', null=True, upload_to='midia'),
        ),
    ]