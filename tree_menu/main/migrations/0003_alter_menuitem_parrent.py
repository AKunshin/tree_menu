# Generated by Django 4.1.7 on 2023-04-26 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_menuitem_options_alter_menuitem_parrent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parrent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='main.menuitem', verbose_name='Parrent item'),
        ),
    ]