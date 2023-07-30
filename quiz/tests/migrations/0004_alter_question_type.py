# Generated by Django 4.2.3 on 2023-07-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('radio', 'Radio'), ('checkbox', 'Checkbox'), ('input', 'Input'), ('select', 'Select')], default='radio', max_length=300),
            preserve_default=False,
        ),
    ]