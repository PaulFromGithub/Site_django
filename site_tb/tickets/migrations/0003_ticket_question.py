# Generated by Django 4.1.5 on 2023-02-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='question',
            field=models.TextField(default='question', verbose_name='Вопрос'),
            preserve_default=False,
        ),
    ]