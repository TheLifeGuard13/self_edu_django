# Generated by Django 5.0.6 on 2024-06-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='chapter/', verbose_name='Превью')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'раздел',
                'verbose_name_plural': 'разделы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='material/', verbose_name='Превью')),
                ('url', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ссылка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'материал',
                'verbose_name_plural': 'материалы',
                'ordering': ['id'],
            },
        ),
    ]
