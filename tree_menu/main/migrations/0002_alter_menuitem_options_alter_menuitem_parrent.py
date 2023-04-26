# Generated by Django 4.1.7 on 2023-04-26 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['parrent_id']},
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parrent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.menuitem', verbose_name='Parrent item'),
        ),
    ]
