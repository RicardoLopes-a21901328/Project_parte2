# Generated by Django 3.2.3 on 2021-05-31 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=200)),
                ('mensagem', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
