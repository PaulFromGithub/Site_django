# Generated by Django 4.1.5 on 2023-03-10 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_delete_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text_question',
            new_name='text_questions',
        ),
    ]