# Generated by Django 4.1.5 on 2023-03-02 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticketanswer_ticketnumber_ticketquestion_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TicketNumber',
            new_name='Ticket',
        ),
        migrations.DeleteModel(
            name='TicketAnswer',
        ),
        migrations.DeleteModel(
            name='TicketQuestion',
        ),
    ]