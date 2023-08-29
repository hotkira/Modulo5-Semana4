# Generated by Django 4.2.4 on 2023-08-22 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_reservadebanho'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['data'], 'verbose_name': 'Formulário de contato', 'verbose_name_plural': 'Formulários de contatos'},
        ),
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(default=False),
        ),
    ]