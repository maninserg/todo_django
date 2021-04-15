# Generated by Django 3.2 on 2021-04-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_lists', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='', verbose_name='Task'),
        ),
    ]
