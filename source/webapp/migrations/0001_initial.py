# Generated by Django 4.1.7 on 2023-03-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Наименование')),
                ('category', models.CharField(choices=[('OTHER', 'Другое'), ('RIFLES', 'Винтовки'), ('MELEE', 'Ближнее'), ('PISTOLS', 'Пистолеты'), ('SNIPERS', 'Снайперские')], default='OTHER', max_length=100, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images', verbose_name='Фото')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата и время')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
