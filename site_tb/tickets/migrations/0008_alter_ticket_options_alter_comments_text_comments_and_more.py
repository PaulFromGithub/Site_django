# Generated by Django 4.1.5 on 2023-03-07 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_rename_ticketnumber_ticket_delete_ticketanswer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Билет', 'verbose_name_plural': 'Билеты'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='text_comments',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Номер билета'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.TextField(verbose_name='Текст вопроса')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(verbose_name='Текст ответа')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.question', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
