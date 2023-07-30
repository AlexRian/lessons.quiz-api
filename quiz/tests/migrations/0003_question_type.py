# Generated by Django 4.2.3 on 2023-07-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_alter_answer_options_remove_question_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(blank=True, choices=[('Radio', 'radio'), ('Checkboxes', 'checkbox'), ('Input', 'input'), ('Select', 'select')], max_length=300, null=True),
        ),
    ]