# Generated by Django 4.0.3 on 2022-03-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_cause_options_remove_cause_icon_cause_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cause',
            options={'verbose_name': ' Yutuq ', 'verbose_name_plural': 'Bizning yutuqlarimiz'},
        ),
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': 'Malumot', 'verbose_name_plural': ' Malumotlar '},
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.CharField(max_length=500, verbose_name='video url'),
        ),
    ]