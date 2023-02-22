# Generated by Django 4.1.7 on 2023-02-22 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('parrent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.menuitem', verbose_name='Parrent item')),
            ],
            options={
                'ordering': ['parrent__id'],
            },
        ),
    ]
