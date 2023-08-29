# Generated by Django 4.2.4 on 2023-08-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('mensagem', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
